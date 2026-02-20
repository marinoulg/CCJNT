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


## STEP 1: Gather data (manually for now)
From [Teritoires Climats Ademe]("https://www.territoires-climat.ademe.fr/opendata#_blank), create your own csv as input data.


## STEP 2: Run ```make main``` in terminal
This command will:
- Clean data that you may have previously created in another run via the command ```python method/clean_data.py```
- For the same reason, start from a clean slate in terms of outputs with the command ```rm -rf outputs/```
- and finally run the command python ```main.py``` which, in a loop:
  - creates a consolidated csv for each community,
  - charges the csv in cache for each community,
  - get the outputs for each community,
  - generates the presentations for each community.

## Overview of the project's architecture
```
tree -L 1
```

```
.
├── data
│   ├── community.csv
│   └── Demarche_(...).csv
├── method
│   ├── __init__.py
│   ├── clean_data.py
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
├── pptx_dir
│   └── community
│       └── community.pptx
├── README.md
├── requirements.txt
├── setup.py
├── main.py
├── Makefile
└── tests
    └── test_merge_all.py
```
## To-do
- Quand on parle de "Diagnostic" dans merged, dire de quand date le diagnostic en le rajoutant en format subtext
- Quand je rajoute le tableau à droite de chaque slide avec les infos, trier ces infos pour n'afficher que les relevant ones
- Corriger les titres des slides, parfois c'est le nom du directory, parfois le titre du graphe --> homogénéiser
- Corriger problème avec image/diagram pour PM2.5
- Comprendre pourquoi le lien de l'Ademe dans mon README.md n'apparaît pas

## Done
- Comprendre pourquoi parfois j'ai des images en doubles, mais avec un tableau à droite différent en plus (ou au moins, pas dans le même ordre)
- Correct problem outputs - ça fonctionne dans le notebook
- Correct where the .pptx presentations are saved
