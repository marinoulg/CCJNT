# Couche Carbone Jumeaux Numériques de Territoires
## STEP 0: Install the package
1) Clone the repo
```
git clone https://github.com/marinoulg/CCJNT.git
```
2) Create a virtual environment
```
pyenv install 3.12.8 CCJNT
```
3) Set the virtual environment to the local environment
```
pyenv local CCJNT
```
4) Install the package and its dependencies
```
pip install -e .
```


## STEP 1: Gather data
From [Teritoires Climats Ademe]("https://www.territoires-climat.ademe.fr/opendata#_blank), create your own csv as input data.


## STEP 2: Run ```python method/methode_ecologiedatagouvfr.py```
This command allows the user to create the consolidated community's csv, and the outputs (e.g. merged table for the Category for the community, and the diagram in .png format associated to this csv).

## STEP 3: Create automatic PowerPoint presentations
By running:
```
python pptx/presentation.py
```
the presentations will be downloaded in ```pptx/{community_name}/{community.pptx}```


## Overview of the project's architecture
```
tree -L 1
```

```
.
├── data
│   ├── community.csv
│   └── (...).csv
├── method
│   ├── __init__.py
│   ├── methode_ecologiedatagouvfr.py
│   └── params.py
├── notebooks
├── outputs
│   └── community
│       ├── Agriculture
│       ├── Chaleur(en GWh)
│       ├── Consommation_ENR
│       ├── Géothermie
│       ├── Industrie_hors_branche_énergie
│       ├── PEC_CONSO
│       ├── Résidentiel
│       ├── Solaire_photovoltaïque
│       ├── Solaire_thermique
│       ├── (...)
│       └── Tertiaire
├── pptx
│   └── community
│       └── community.pptx
├── README.md
├── requirements.txt
├── setup.py
└── tests
    └── test_merge_all.py
```
## To-do
- Correct problem outputs
- Correct where the .pptx presentations are saved
- Quand on parle de "Diagnostic" dans merged, dire de quand date le diagnostic en le rajoutant en format subtext
- Quand je rajoute le tableau à droite de chaque slide avec les infos, trier ces infos pour n'afficher que les relevant ones
- Corriger les titres des slides, parfois c'est le nom du directory, parfois le titre du graphe --> homogénéiser
- Corriger problème avec image/diagram pour PM2.5
- Comprendre pourquoi le lien de l'Ademe dans mon README.md n'apparaît pas

## Done
- Comprendre pourquoi parfois j'ai des images en doubles, mais avec un tableau à droite différent en plus (ou au moins, pas dans le même ordre)
