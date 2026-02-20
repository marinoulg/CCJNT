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
