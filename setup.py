from setuptools import find_packages
from setuptools import setup

# with open("requirements.txt") as f:
#     content = f.readlines()
# requirements = [x.strip() for x in content if "git+" not in x]

setup(name='ecologiedatagouvfr_PCAET',
      version="0.0.1",
      description="""
      Les données saisies sur Territoires&Climat, dont les données des PCAET, sont disponibles sur la page Open Data du site Territoires&Climat et sur data.ademe.fr. Cet article présente les différents jeux de données disponibles et comment les utiliser.

Rédigé par ADEME le 26/07/2021 | Mis à jour le 15/09/2022 à 15:26:27

L’ADEME met à disposition l’ensemble des données saisies sur Territoires&Climat en open data, dont les données des PCAET. Plusieurs jeux de données sont ainsi disponibles sur la page Data Territoires&Climat ainsi que sur le portail Open Data de l’ADEME, qui permet une meilleure réutilisation (notamment via API). Tous les jeux de données sont actualisés quotidiennement.

Afin de faciliter l’exploitation des données, la description détaillée du contenu de chaque fichier est disponible dans le fichier « Notice d’exploitation des données ».

Données des PCAET déposés par les collectivités

Ces données correspondent aux éléments renseignés par les collectivités lors du dépôt de leur PCAET. Elles sont séparées en plusieurs fichiers, correspondant aux différentes parties du formulaire de dépôt. Les fichiers V2 concernent les PCAET déposés avec le nouveau formulaire de dépôt mis en place au printemps 2020, et les fichiers V1 concernent les PCAET déposés avant cette date.

from: https://www.territoires-climat.ademe.fr/actualite/comment-exploiter-les-donnees-territoires-climat-disponibles-en-open-data

      """,
      license="MIT",
      author_email="marine.le-gall@cerema.fr",
    #   install_requires=requirements,
      packages=find_packages(),
    #   test_suite="tests"
        )
