import os

# ------------------ from .env------------------
GITHUB_NAME = os.environ.get("GITHUB_NAME","marinoulg")
if GITHUB_NAME == "":
    raise ValueError("GITHUB_NAME not found in .env")

"""
attention:
need to do
    '''direnv allow . ''' in terminal
to instantiate the environment
and
    ''' direnv reload'''
every time an environment variable (from .env) has been modified
"""

# ------------------ local variables ------------------
LOCAL_PATH_REPO = os.path.join(os.path.expanduser('~'),"code", GITHUB_NAME,"couche_carbone_des_territoires", "ecologiedatagouvfr_pcaet")
LOCAL_DATA_PATH = os.path.join(LOCAL_PATH_REPO,"data")
LOCAL_PATH_OUTPUTS = os.path.join(LOCAL_PATH_REPO,"outputs")

PCAET_DIR = os.path.join(LOCAL_DATA_PATH,"PCAETs")
PCAET_DATA = os.path.join(PCAET_DIR,"data")
PCAET_V1_DATA = os.path.join(PCAET_DATA,"PCAET_V1")
PCAET_V2_DATA = os.path.join(PCAET_DATA,"PCAET_V2")

DEMARCHES = os.path.join(PCAET_DIR, "Demarches")
DEMARCHES_PCAET_V1 = os.path.join(DEMARCHES, "PCAET_V1")
DEMARCHES_PCAET_V2 = os.path.join(DEMARCHES, "PCAET_V2")

PATH_DATA_WIP = os.path.join(PCAET_DIR, "WIP")

COMMUNITIES_WIP = [
    "La Rochelle",
    "Valenciennes",
    "Paris"
    ]

COMMUNITIES = {
        "La_Rochelle":{
            # "idx_of_local_authority":1,
            "PATH":os.path.join(LOCAL_DATA_PATH,"valenciennes.csv"),
                    },
        "Valenciennes":{
            # "idx_of_local_authority":2,
            "PATH":os.path.join(LOCAL_DATA_PATH,"la_rochelle.csv"),
                        }
                }

DEMARCHES = {
    "Demarches_PCAET_V1_pec_seq":"Extraction des Profils Energie Climat – Séquestration des démarches PCAET V1",
    "Demarches_PCAET_V2_pec_seq":"Extraction des Profils Energie Climat – Séquestration des démarches PCAET V2",
    "Demarches_PCAET_V1_enr":"Extraction des données du diagnostic territorial et des objectifs du territoire pour les énergies renouvelables des démarches PCAET V1",
    "Demarches_PCAET_V2_enr":"Extraction des données du diagnostic territorial et des objectifs du territoire pour les énergies renouvelables des démarches PCAET V2",
    "Demarches_PCAET_V1_polluant":"Extraction des données des polluants des démarches de type PCAET V1",
    "Demarches_PCAET_V2_polluant":"Extraction des données des polluants des démarches de type PCAET V2"
    }

INFORMATIONS = {
    # Profil Energie climat - Emission GES (1)
"PEC_Emission_GES_Annee_Compta":"Année de comptabilisation des émissions GES si diagnostic",
"PEC_GES_<Code Secteur>_<CodePeriode>":"""Emission GES en TeqCO2, pour chaque secteur (8 secteurs), à savoir:
""1"",""Résidentiel""
""2"",""Tertiaire""
""3"",""Transport routier""
""4"",""Autres transports""
""5"",""Agriculture""
""6"",""Déchets""
""7"",""Industrie hors branche énergie""
""8"",""Industrie  branche énergie""
et chaque période (4 périodes)
""1"", ""Diagnostic""
""3"", ""2026""
""6"", ""2030""
""7"", ""2050""
""",

    # Profil Energie climat - Consommation énergétique (1)
"PEC_Consommation_Annee_Compta":"Année de comptabilisation de la consommation  énergétique si diagnostic",
"PEC_CONSO_<Code Secteur>_<CodePeriode>":"""Consommation énergie en GWh, pour chaque secteur (8 secteurs), à savoir:
""1"",""Résidentiel""
""2"",""Tertiaire""
""3"",""Transport routier""
""4"",""Autres transports""
""5"",""Agriculture""
""6"",""Déchets""
""7"",""Industrie hors branche énergie""
""8"",""Industrie  branche énergie""
et chaque période (4 périodes)
""1"", ""Diagnostic""
""3"", ""2026""
""6"", ""2030""
""7"", ""2050""
""",
"PEC_GES_CONSO_commentaire":"Commentaires sur les données d'émission de GES et les consommations énergétiques",

    # Profil Energie climat -Vulnérabilité (4)
"PEC_DomaineVulnerabilite_<Numéro Ligne Domaine Vulnérabilité>":"""Vulnérabilités sur le territoire.
3 colonnes pour chaque type de vulnérabilité (numéro de ligne) :
- domaine de vulnérabilité
- description de la vulnérabilité
- description des objectifs fixés
""",
"PEC_Vulnerabilite_<Numéro Ligne Domaine Vulnérabilité>":"",
"PEC_Vulnerabilite_Objectif_fixe_<Numéro Ligne Domaine Vulnérabilité>":"",
"PEC_Vulnerabilite_commentaire":"",

    # Séquestration (2)
"SEQ_<Code Sol et forêt>_Estimation_Sequestration_nette_CO2":"""Estimation de la séquestration nette de CO2 sur le territoire pour chaque type de sol
Ci-dessous la liste des codes ""Sol et Forêt""
""1"",""Forêt""
""2"",""Terre cultivées et prairies""
""3"",""Autres sols""
""",
"SEQ_<Code Sol et forêt>_Estimation_Annee":"Année de l'estimation pour chaque type de sol",
"SEQ_<Code Sol et forêt>_Possibilite_Developpement_nette_CO2":"Estimation du potentiel de développement de la séquestration nette de CO2 pour chaque type de sol",
"SEQ_<Code Sol et forêt>_Possibilite_Developpement_annee":"Année à laquelle le potentiel de développement de la séquestration pourrait être atteint pour chaque type de sol",
"SEQ_commentaire":"Commentaire sur le tableau des données de séquestration",

    # Objectifs de renforcements de la séquestration
"Vegetation objectif":"Objectifs de renforcement du stockage de carbone sur la végétation, dans les sols, dans les bâtiments et sur d’autres cibles ainsi que les années de références respectives.",
"Vegetation année de reference":"",
"Sols objectif":"",
"Sols année de reference":"",
"Bâtiments objectif":"",
"Bâtiments année de reference":"",
"Autres cibles objectif":"",
"Autres cibles année de reference":"",
"Production biosourcée <Numéro_ligne >":"""Objectifs de production biosourcée à usage autre qu'alimentaire.
3 colonnes pour chaque type de production (numéro de ligne) :
- type de production
- description de l'objectif
- année de référence"
""",
"Objectif <Numéro_ligne >":"",
"Année de reference <Numéro_ligne >":"",

"ENR_<Code filiere>_Diag_Annee_Compta":"""Année de comptabilisation de la production ENR pour chaque filière
Ci-dessous la liste des filieres (avec code type filiere)
""1"",""1"",""Eolien terrestre"", ""Electricité (en GWh)""
""2"",""1"",""Solaire photovoltaïque"", ""Electricité (en GWh)""
""3"",""1"",""Solaire thermodynamique"", ""Electricité (en GWh)""
""4"",""1"",""Hydraulique"", ""Electricité (en GWh)""
""5"",""1"",""Biomasse solide"", ""Electricité (en GWh)""
""6"",""1"",""Biogaz"", ""Electricité (en GWh)""
""7"",""1"",""Géothermie"", ""Electricité (en GWh)""
""8"",""2"",""Biomasse solide"", ""Chaleur (en GWh)""
""9"",""2"",""Pompes à chaleur"", ""Chaleur (en GWh)""
""10"",""2"",""Géothermie"", ""Chaleur (en GWh)""
""11"",""2"",""Solaire thermique"", ""Chaleur (en GWh)""
""12"",""2"",""Biogaz"", ""Chaleur (en GWh)""
""13"",""3"",""Biométhane (en GWh)"", ""Biométhane (en GWh)""
""14"",""4"",""Biocarburants (en GWh)"", ""Biocarburants (en GWh)""
""",
"ENR_<Code filiere>_<Code période>_Production":"""Production des ENR pour 8 filières
Ci-dessous la liste des filières (avec code type filière)
""1"",""1"",""Eolien terrestre""
""2"",""1"",""Solaire photovoltaïque""
""3"",""1"",""Solaire thermodynamique""
""4"",""1"",""Hydraulique""
""5"",""1"",""Biomasse solide""
""6"",""1"",""Biogaz""
""7"",""1"",""Géothermie""
""13"",""3"",""Biométhane (en GWh)""
et pour chaque période (4)
""1"", ""Diagnostic""
""3"", ""2026""
""6"", ""2030""
""7"", ""2050""
""",
"ENR_<Code filiere>_<Code période>_Consommation":"""Production des ENR pour 6 filières
Ci-dessous la liste des filières (avec code type filière)
""8"",""2"",""Biomasse solide""
""9"",""2"",""Pompes à chaleur""
""10"",""2"",""Géothermie""
""11"",""2"",""Solaire thermique""
""12"",""2"",""Biogaz""
""14"",""4"",""Biocarburants (en GWh)""
et pour chaque période (4)
""1"", ""Diagnostic""
""3"", ""2026""
""6"", ""2030""
""7"", ""2050""

NB: pas de données de consommation ENR pour la période de diagnostic
""",
"ENR_valorisation_recuperation_<Code période>":"""Valorisation du potentiel d'énergie de récupération (en GWh) pour les périodes hors diagnostic (3 périodes)
""3"", ""2026""
""6"", ""2030""
""7"", ""2050""
""",
"ENR_valorisation_stockage_<Code période>":"""Valorisation du potentiel de stockage énergétique  (en GWh) pour les périodes hors diagnostic (3 périodes)
""3"", ""2026""
""6"", ""2030""
""7"", ""2050""
""",
"ENR_commentaire":"Commentaire sur les données ENR",


    # Polluant
"POL_<Code Secteur>_<Code période>_<Code Polluant>":"""Diagnostic ou objectif des émissions de polluants par secteur(8)
""1"", ""Résidentiel""
""2"", ""Tertiaire""
""3"", ""Transport routier""
""4"", ""Autres transports""
""5"", ""Agriculture""
""6"", ""Déchets""
""7"", ""Industrie hors branche énergie""
""8"", ""Industrie branche énergie""
par période (4)
""1"", ""Diagnostic""
""3"", ""2026""
""6"", ""2030""
""7"", ""2050""
et par polluant(6)
""1"", ""PM10""
""2"", ""PM2,5""
""3"", ""Oxydes d'azote""
""4"", ""Dioxyde de soufre""
""5"", ""COV""
""6"", ""NH3""
""",
"POL_<Code Polluant>_Diag_Annee_compta":"Année de comptabilisation par polluant pour la période de diagnostic",
"TOTAL_POL_<Code Polluant>_<Code période>":"Total des émissions de polluants <Code Polluant> par période (4)",
"POL_Commentaire":"Commentaire sur les données d'émissions de polluants",

"date_creation":"Date de création de la démarche sur Territoires&Climat",
"date_modification":"Date de la dernière modification de la démarche",
"date_lancement":"Date de lancement de la démarche",
"type_demarche":"Liste des types de démarches (hors PCAET)",
"nom":"nom de la démarche",
"description_rapide":"Description de la démarche",
"collectivites_coporteuses":"Liste des collectivités SIREN-Nom collectivités",
"population_couverte":"Population couverte par les collectivités porteuses",
"demarche_etat":"Non renseigné (pas de gestion de l'état d'avancement pour les démarches libres)",
"Chef_de_projet":"Prénom, nom du chef de projet",
"Contact":"Liste des contacts nom prénom et rôle",
"elu_referent":"Nom de l'élu référent en saisie libre",
"commentaire_statut":"Commentaire",
"date_reception_projet":"",
"date_envoi_avis_dreal":"Non renseigné",
"date_envoi_avis_cr":"Non renseigné",
"oblige":"Non renseigné",
"Autres_démarches_hors_EC":"""Liste des autres démarches hors énergie climat sur le territoire : "agenda 21", "PLUI", …""",
"Autres_démarches":"Liste des autres démarches énergie climat sur le territoire. Liste des numéros de démarche de la liste",


"PEC_Annee_Echeance_Obj":"Année de comptabilisation des émissions GES si diagnostic",
"PEC_GES_Diagnostic_<Code Secteur>":"""Emission GES en TeqCO2, pour chaque secteur (8 secteurs)
""1"",""Résidentiel""
""2"",""Tertiaire""
""3"",""Transport routier""
""4"",""Autres transports""
""5"",""Agriculture""
""6"",""Déchets""
""7"",""Industrie hors branche énergie""
""8"",""Industrie  branche énergie""
""",
"PEC_GES_Objectif_<Code Secteur>":"""Emission GES en TeqCO2, pour chaque secteur (8 secteurs)
""1"",""Résidentiel""
""2"",""Tertiaire""
""3"",""Transport routier""
""4"",""Autres transports""
""5"",""Agriculture""
""6"",""Déchets""
""7"",""Industrie hors branche énergie""
""8"",""Industrie  branche énergie""
""",

"PEC_CONSO_Annee_Echeance_Obj":	"Année de comptabilisation de la consommation  énergétique si diagnostic",
"PEC_CONSO_Diagnostic_<Code secteur>":	"""Consommation énergie en GWh, pour chaque secteur (8 secteurs)
""1"",""Résidentiel""
""2"",""Tertiaire""
""3"",""Transport routier""
""4"",""Autres transports""
""5"",""Agriculture""
""6"",""Déchets""
""7"",""Industrie hors branche énergie""
""8"",""Industrie  branche énergie""
""",
"PEC_CONSO_Objectif_<Code secteur>":"""Objectif de maîtrise des consommations énergétiques en GWh pour chaque secteur (8 secteurs)
""1"",""Résidentiel""
""2"",""Tertiaire""
""3"",""Transport routier""
""4"",""Autres transports""
""5"",""Agriculture""
""6"",""Déchets""
""7"",""Industrie hors branche énergie""
""8"",""Industrie  branche énergie""
""",
"PEC_GES_CONSO_commentaire":"Commentaires sur les données d'émission de GES et les consommations énergétiques",




"ENR_Annee_Echeance_Obj":"Année de comptabilisation des objectifs de production et consommation des ENR",
"ENR_<Code type filiere>_Diagnostic_Production":"""Diagnostic de production et objectif de production des ENR par type de filière.
    2 type de filière sont concernées :
    1; Electricité
    2; chaleur"
    """,
"ENR_<Code type filiere>_Objectif_Production":"",
"ENR_<Code type filiere>_Diagnostic_Production":"",
"ENR_<Code type filiere>_Objectif_Production":"",
"ENR_commentaire":"",



"PEC_Vulnerabilite_<Code Domaine vulnérabilité>":"""Description de la vulnérabilité sur le territoire pour chaque domaine
""1"",""Agriculture""
""2"",""Aménagement / urbanisme (y compris grandes infrastructures, voirie)""
""3"",""Biodiversité (y compris milieux naturels)""
""4"",""Déchets""
""5"",""Eau (Approvisionnement en eau, assainissement, cours d'eau et ruissellement des eaux de pluie)""
""6"",""Espaces verts""
""7"",""Forêt ""
""8"",""Gestion, production et distribution de l'énergie (y compris approvisionnement en énergie)""
""9"",""Industrie""
""10"",""Littoral""
""11"",""Résidentiel""
""12"",""Santé""
""13"",""Sécurité Civile""
""14"",""Tertiaire (y compris patrimoine bâti de la collectivité)""
""15"",""Tourisme""
""16"",""Transport (y compris routier)""
""",
"PEC_Vulnerabilite_Objectif_fixe_<Code Domaine vulnérabilité>":"Description des objectifs fixés sur le territoire pour chaque domaine",


}
