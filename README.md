
# Application Web de Gestion et Visualisation de Données

## Description

Cette application web est conçue pour gérer le téléchargement, le stockage, l'analyse et la visualisation de fichiers Excel. Elle permet aux utilisateurs de télécharger des fichiers, de sélectionner des colonnes pour l'analyse, de générer des statistiques descriptives et de créer des visualisations graphiques. L'application permet également de gérer les valeurs manquantes et de normaliser les données en vue d'une utilisation future dans des projets d'intelligence artificielle. Les utilisateurs peuvent extraire les colonnes importantes et télécharger les données transformées.

## Fonctionnalités

### 1. Téléchargement de fichiers
Les utilisateurs peuvent télécharger des fichiers Excel depuis leur ordinateur. L'application accepte les fichiers Excel et les stocke de manière sécurisée dans le répertoire de téléchargement.

#### Étapes pour télécharger un fichier
- Ouvrez l'application dans votre navigateur.
- Cliquez sur le bouton "Télécharger un fichier".
- Sélectionnez le fichier que vous souhaitez télécharger depuis votre ordinateur.
- Cliquez sur "Soumettre" pour télécharger le fichier.

### 2. Sélection de colonnes et analyse statistique
Après avoir téléchargé un fichier, les utilisateurs peuvent sélectionner les colonnes qu'ils souhaitent analyser. L'application génère des statistiques descriptives pour les colonnes sélectionnées, telles que la moyenne, la médiane, l'écart type, etc.

#### Étapes pour analyser des colonnes
- Sélectionnez les colonnes à analyser à partir de la liste des colonnes disponibles.
- Cliquez sur "Générer des statistiques" pour voir les statistiques descriptives des colonnes sélectionnées.

### 3. Visualisation des données
Les utilisateurs peuvent créer différentes visualisations graphiques, y compris des histogrammes, des diagrammes en barres, des heatmaps, etc., en sélectionnant les colonnes appropriées et le type de graphique.

#### Étapes pour créer des visualisations
- Sélectionnez les colonnes pour la visualisation.
- Choisissez le type de graphique souhaité (histogramme, diagramme en barres, heatmap, etc.).
- Cliquez sur "Générer le graphique" pour voir la visualisation.

### 4. Gestion des valeurs manquantes et normalisation
L'application permet aux utilisateurs de gérer les valeurs manquantes dans les données en les remplissant avec la moyenne ou en les supprimant. De plus, les utilisateurs peuvent normaliser les données pour les préparer à une utilisation future dans des projets d'intelligence artificielle.

#### Étapes pour gérer les valeurs manquantes et normaliser les données
- Sélectionnez les colonnes pour la gestion des valeurs manquantes et la normalisation.
- Choisissez l'option de gestion des valeurs manquantes (remplir avec la moyenne ou supprimer les lignes).
- Cliquez sur "Appliquer la normalisation" pour normaliser les données.

### 5. Extraction et téléchargement des données transformées
Les utilisateurs peuvent extraire les colonnes importantes et télécharger les données transformées après avoir sélectionné et éventuellement normalisé certaines colonnes. Les données sont exportées dans un fichier Excel.

#### Étapes pour télécharger les données transformées
- Sélectionnez les colonnes à inclure dans le fichier exporté.
- Cliquez sur "Télécharger les données" pour obtenir le fichier Excel des données transformées.

## Installation

### Prérequis

- Python 3.x
- pip (gestionnaire de paquets Python)
- Virtualenv (optionnel mais recommandé)

### Étapes d'installation

1. **Cloner le dépôt ou télécharger les fichiers sources**
   - Assurez-vous d'avoir les fichiers sources de l'application. Si vous avez un fichier zip, extrayez-le.

2. **Créer un environnement virtuel (optionnel mais recommandé)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows: venv\Scripts\activate
   ```

3. **Installer les bibliothèques requises**
   - Accédez au répertoire où se trouvent les fichiers sources (par exemple, le dossier `py` extrait) et installez les dépendances requises.

#### Liste des bibliothèques requises et leur installation
- **Flask** : Framework web utilisé pour créer l'application web.
  ```bash
  pip install Flask
  ```
- **pandas** : Utilisé pour la manipulation et l'analyse des données.
  ```bash
  pip install pandas
  ```
- **matplotlib** : Utilisé pour créer des visualisations graphiques.
  ```bash
  pip install matplotlib
  ```
- **scikit-learn** : Utilisé pour la normalisation des données.
  ```bash
  pip install scikit-learn
  ```
- **scipy** : Utilisé pour les calculs statistiques.
  ```bash
  pip install scipy
  ```
- **seaborn** : Utilisé pour améliorer les visualisations graphiques.
  ```bash
  pip install seaborn
  ```

## Utilisation

1. **Lancer l'application**
   - Exécutez le fichier principal de l'application.
   ```bash
   python app.py
   ```

2. **Accéder à l'application**
   - Ouvrez votre navigateur web et accédez à l'URL suivante :
   ```
   http://127.0.0.1:5000
   ```

3. **Utiliser les fonctionnalités**
   - **Télécharger des fichiers** : Utilisez le formulaire de téléchargement pour ajouter de nouveaux fichiers.
   - **Sélectionner des colonnes et analyser des données** : Sélectionnez les colonnes pour générer des statistiques descriptives.
   - **Visualiser les données** : Créez des graphiques pour visualiser les données.
   - **Gérer les valeurs manquantes et normaliser les données** : Gérez les valeurs manquantes et normalisez les données pour une utilisation future dans des projets d'IA.
   - **Télécharger les données transformées** : Téléchargez les données après transformation dans un fichier Excel.

## Structure du projet

- `app.py` : Le fichier principal de l'application qui contient le code Flask.
- `static/` : Ce dossier contient les fichiers statiques comme les CSS, JavaScript, images, etc.
- `templates/` : Ce dossier contient les templates HTML utilisés par l'application.
- `uploads/` : Ce dossier est destiné à stocker les fichiers téléchargés par les utilisateurs.

## Technologies utilisées

- **Python** : Langage principal utilisé pour le développement.
- **Flask** : Framework web utilisé pour créer l'application web.
- **pandas** : Utilisé pour la manipulation et l'analyse des données.
- **matplotlib** : Utilisé pour créer des visualisations graphiques.
- **scikit-learn** : Utilisé pour la normalisation des données.
- **scipy** : Utilisé pour les calculs statistiques.
- **seaborn** : Utilisé pour améliorer les visualisations graphiques.
