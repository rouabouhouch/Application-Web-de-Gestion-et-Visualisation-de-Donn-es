from flask import Flask, request, render_template, send_file, jsonify
import pandas as pd
import os
import matplotlib
matplotlib.use('Agg')  # Set the backend to Agg
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import io
import logging
import numpy as np
from scipy.stats import skew, kurtosis
import seaborn as sns

app = Flask(__name__, static_folder='static')

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def upload_file():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'Aucun fichier sélectionné'
    file = request.files['file']
    if file.filename == '':
        return 'Aucun fichier sélectionné'
    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        df = pd.read_excel(filepath)
        columns = df.columns.tolist()
        return render_template('select_columns.html', columns=columns, filename=file.filename)

@app.route('/statistics', methods=['POST'])
def statistics():
    selected_columns = request.form.getlist('columns')
    filename = request.form['filename']
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    df = pd.read_excel(filepath)

    stats = []

    for col in selected_columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            column_data = df[col].dropna()  # Handle missing values
            stat = {
                'column': col,
                'mean': column_data.mean(),
                'median': column_data.median(),
                'std': column_data.std(),
                'min': column_data.min(),
                'max': column_data.max(),
                'variance': column_data.var(),
                'skewness': skew(column_data),
                'kurtosis': kurtosis(column_data)
            }
            stats.append(stat)
        else:
            stats.append({'column': col, 'message': 'Colonne non numérique'})

    return jsonify(stats)

@app.route('/visualization', methods=['POST'])
def visualization():
    selected_columns = request.form.getlist('columns')
    chart_type = request.form['chart_type']
    filename = request.form['filename']
    
    logging.debug(f"Selected columns: {selected_columns}")
    logging.debug(f"Chart type: {chart_type}")
    logging.debug(f"Filename: {filename}")

    filepath = os.path.join(UPLOAD_FOLDER, filename)
    df = pd.read_excel(filepath)
    
    numeric_columns = [col for col in selected_columns if pd.api.types.is_numeric_dtype(df[col])]
    categorical_columns = [col for col in selected_columns if not pd.api.types.is_numeric_dtype(df[col])]

    plt.figure()

    if chart_type == 'hist' and len(numeric_columns) == 1:
        plt.hist(df[numeric_columns[0]].dropna(), bins=20, alpha=0.7, color='blue')
        plt.xlabel(numeric_columns[0])
        plt.ylabel('Fréquence')
        plt.title(f'Histogramme de {numeric_columns[0]}')
    elif chart_type == 'scatter' and len(numeric_columns) == 2:
        plt.scatter(df[numeric_columns[0]], df[numeric_columns[1]])
        plt.xlabel(numeric_columns[0])
        plt.ylabel(numeric_columns[1])
        plt.title('Nuage de points')
    elif chart_type == 'line' and len(numeric_columns) == 2:
        df.dropna(subset=numeric_columns, inplace=True)
        df.sort_values(by=numeric_columns[0], inplace=True)
        plt.plot(df[numeric_columns[0]], df[numeric_columns[1]])
        plt.xlabel(numeric_columns[0])
        plt.ylabel(numeric_columns[1])
        plt.title('Graphique linéaire')
    elif chart_type == 'boxplot' and len(numeric_columns) > 0:
        df[numeric_columns].plot(kind='box')
        plt.title('Boxplot des colonnes sélectionnées')
    elif chart_type == 'barplot' and len(categorical_columns) == 1:
        df[categorical_columns[0]].value_counts().plot(kind='bar')
        plt.xlabel(categorical_columns[0])
        plt.ylabel('Fréquence')
        plt.title(f'Barplot de {categorical_columns[0]}')
    elif chart_type == 'piechart' and len(categorical_columns) == 1:
        df[categorical_columns[0]].value_counts().plot(kind='pie', autopct='%1.1f%%')
        plt.title(f'Pie Chart de {categorical_columns[0]}')
    elif chart_type == 'heatmap' and len(numeric_columns) > 1:
        correlation_matrix = df[numeric_columns].corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
        plt.title('Heatmap des corrélations')
    else:
        return 'Type de graphique ou nombre de colonnes sélectionnées incorrects'

    plt.tight_layout()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    return send_file(img, mimetype='image/png')

@app.route('/download', methods=['POST'])
def download():
    selected_columns = request.form.getlist('columns')
    filename = request.form['filename']
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    df = pd.read_excel(filepath)

    new_df = pd.DataFrame()

    for col in selected_columns:
        new_col_name = request.form[f'rename_{col}']
        if col in request.form.getlist('normalize') and pd.api.types.is_numeric_dtype(df[col]):
            scaler = MinMaxScaler()
            new_df[new_col_name] = pd.Series(scaler.fit_transform(df[[col]].fillna(df[col].mean())).flatten())
        else:
            missing_value_option = request.form.get(f'missing_{col}', 'leave')
            if missing_value_option == 'mean':
                new_df[new_col_name] = df[col].fillna(df[col].mean())
            elif missing_value_option == 'remove':
                df = df.dropna(subset=[col])
                new_df = df[selected_columns].copy()
                break
            else:
                new_df[new_col_name] = df[col]

    output_path = os.path.join(UPLOAD_FOLDER, 'colonnes_extraites.xlsx')
    new_df.to_excel(output_path, index=False)
    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

