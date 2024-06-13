// Function for opening tabs with transition effects
function openTab(evt, tabName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    var currentTab = document.getElementById(tabName);
    currentTab.style.display = "block";
    currentTab.style.opacity = 0; // Initially set opacity to 0
    setTimeout(() => {
        currentTab.style.opacity = 1; // Apply transition by setting opacity to 1
    }, 10);
    evt.currentTarget.className += " active";
}

function showStatistics() {
    const form = document.getElementById('column-form');
    const formData = new FormData(form);
    fetch('/statistics', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const statsDiv = document.getElementById('statistics');
        let html = '<h2>Statistiques Résumées</h2>';
        html += '<table>';
        html += '<tr><th>Colonne</th><th>Moyenne</th><th>Médiane</th><th>Écart Type</th><th>Min</th><th>Max</th><th>Variance</th><th>Asymétrie</th><th>Aplatissement</th></tr>';
        data.forEach(stat => {
            if (stat.message) {
                html += `<tr><td>${stat.column}</td><td colspan="8">${stat.message}</td></tr>`;
            } else {
                html += `<tr><td>${stat.column}</td><td>${stat.mean}</td><td>${stat.median}</td><td>${stat.std}</td><td>${stat.min}</td><td>${stat.max}</td><td>${stat.variance}</td><td>${stat.skewness}</td><td>${stat.kurtosis}</td></tr>`;
            }
        });
        html += '</table>';
        // Ajoutez une animation de fondu
        statsDiv.innerHTML = html;
        statsDiv.style.opacity = 0;
        setTimeout(() => {
            statsDiv.style.opacity = 1;
        }, 100);
    });
}

function generateVisualization(event) {
    event.preventDefault();
    const form = document.getElementById('visualization-form');
    const formData = new FormData(form);
    fetch('/visualization', {
        method: 'POST',
        body: formData
    })
    .then(response => response.blob())
    .then(blob => {
        const url = URL.createObjectURL(blob);
        const visualDiv = document.getElementById('statistics-visualize');
        visualDiv.innerHTML = '<h2>Visualisation</h2><img src="' + url + '" class="zoomIn">';
        visualDiv.classList.add('zoomIn'); // Adding zoom-in animation class
    });
}

function showChartDescription() {
    const chartType = document.getElementById('chart_type').value;
    const descriptionDiv = document.getElementById('chart-description');
    let description = '';

    switch (chartType) {
        case 'hist':
            description = 'Histogramme: Sélectionnez 1 colonne numérique.';
            break;
        case 'scatter':
            description = 'Nuage de points: Sélectionnez 2 colonnes numériques.';
            break;
        case 'line':
            description = 'Graphique linéaire: Sélectionnez 2 colonnes numériques.';
            break;
        case 'boxplot':
            description = 'Boxplot: Sélectionnez une ou plusieurs colonnes numériques.';
            break;
        case 'barplot':
            description = 'Barplot: Sélectionnez 1 colonne catégorielle.';
            break;
        case 'piechart':
            description = 'Pie Chart: Sélectionnez 1 colonne catégorielle.';
            break;
        case 'heatmap':
            description = 'Heatmap: Sélectionnez 2 colonnes numériques ou plus.';
            break;
        default:
            description = '';
    }

    descriptionDiv.innerHTML = `<p>${description}</p>`;
}

function toggleMolecularWeightInput(column, value) {
    var inputDiv = document.getElementById('molecular_weight_input_' + column);
    if (value === 'g/L_to_mol/L') {
        inputDiv.style.display = 'block';
    } else {
        inputDiv.style.display = 'none';
    }
}

// Function for cool hover effect on buttons
const button = document.getElementById('myButton');
button.addEventListener('mouseover', () => {
  button.style.backgroundColor = 'red'; // Change color on hover
});
button.addEventListener('mouseout', () => {
  button.style.backgroundColor = 'blue'; // Revert back to original color
});

document.querySelectorAll('select[name^="missing_"]').forEach(function(select) {
    select.addEventListener('change', function() {
        var method = this.value;
        var constantInput = this.parentElement.querySelector('input[name^="constant_"]');
        if (constantInput) {
            constantInput.style.display = method === 'constant' ? 'block' : 'none';
        }
    });
});

