import pandas as pd
import numpy as np
import os

from ecologiedatagouvfr_PCAET.params import LOCAL_DATA_PATH
from params import LOCAL_DATA_PATH

# ------------------- Context - broad Information ---------------
"""
Les fichiers « Démarches PCAET [V1 ou V2] ENTETE » comprennent les informations
générales sur les PCAET : collectivité porteuse, dates, état d’avancement,
description…
"""

# ---------------------- Generic functions ----------------------
to_be_mapped = [
            "Diagnostic",
            "2026",
            "2030",
            "2050",
            "Résidentiel",
            "Tertiaire",
            "Transports_routiers",
            "Autres_transports",
            "Agriculture",
            "Déchets",
            "Industrie_hors_branche_énergie",
            "Industrie_branche_énergie",
            "Eolien_terrestre",
            "Solaire_photovoltaïque",
            "Solaire_thermodynamique",
            "Hydraulique",
            "Biomasse_solide",
            "Biogaz",
            "Géothermie",
            "Biomasse_solide",
            "Pompes_à_chaleur",
            "Géothermie",
            "Solaire_thermique",
            "Biogaz",
            "Biométhane(en GWh)",
            "Biocarburants(en GWh)"
            "Electricité(en GWh)",
            "Chaleur(en GWh)",
            "Biométhane(en GWh)",
            "Biocarburants(en GWh)",
            "PM10",
            "PM2.5",
            "Oxydes_d_azote",
            "Dioxyde_de_soufre",
            "COV",
            "NH3",
            "Polluant_generic",
            "Polluant_Diag_Annee",
            "TOTAL_POL",
            "PEC_GES",
            "PEC_CONSO",
            "SEQ",
            "Diag_Annee_Compta",
            "Production",
            "Consommation",
            "valorisation_recuperation",
            "valorisation_stockage",
        ]

def load_data(csv="Demarches_PCAET_V2_PEC_SEQ.csv",
              nb_of_lines=2,
              idx_of_local_authority=1,
              local_authority_name = "La_Rochelle"):

    csv_path = os.path.join(LOCAL_DATA_PATH,csv)
    df = pd.read_csv(csv_path, sep=";").iloc[:nb_of_lines,:]
    larochelle = df.iloc[idx_of_local_authority-1:idx_of_local_authority,:].T.rename(columns={idx_of_local_authority-1:f"{local_authority_name}"})
    return larochelle

def about_secteur(secteur):
    """
    Mapps n1 for secteurs:
        - PEC_GES and PEC_CONSO
        - polluants
    """
    secteur_dict = {
        "1":"Résidentiel",
        "2":"Tertiaire",
        "3":"Transport_routier",
        "4":"Autres_transports",
        "5":"Agriculture",
        "6":"Déchets",
        "7":"Industrie_hors_branche_énergie",
        "8":"Industrie_branche_énergie",
    }

    for key in secteur_dict:
        if secteur == key:
            return secteur_dict[key]

def about_periode(periode):
    """
    Mapps n2 for all periods,
    for Demarches_PCAET_V2_PEC_SEQ:
        - PEC_GES,
        - PEC_CONSO,
    for Demarches_PCAET_V2_ENR:
        - production_,
        - consommation_,
        - valorisation_recuperation,
        - valorisation_stockage
    for polluants:
        - all
    """
    periode_dict = {
        "1":"Diagnostic",
        "3":"2026",
        "6":"2030",
        "7":"2050",
    }

    for key in periode_dict:
        if periode == key:
            return periode_dict[key]

def for_specific_year_or_sector(tofind, larochelle):
    _2026 = []
    for i,elem in enumerate(larochelle.index):
        if tofind in elem:
            _2026.append(larochelle.iloc[i,:1].values[0])
        else:
            _2026.append(False)

    return _2026

def which_category(cat, larochelle,columns=None):
    return larochelle[larochelle[cat] == True].iloc[:,:1]

def which_cols_and_indexes(df_consolidated,
                           according_to:str,
                           cols=None,
                           ):
    """
    """
    def tmp_what_to_do_with_cols(df_consolidated,
                           according_to:str,
                           cols):
        tmp_df = df_consolidated[cols].reset_index()
        indexes_i_want = []

        for idx, elem in enumerate(tmp_df["index"]):
            if according_to in elem:
                indexes_i_want.append(idx)

        tmp = tmp_df.iloc[indexes_i_want,:].set_index("index")
        tmp = tmp[tmp.loc[:,:]!=False].dropna(axis="index", how="all").dropna(axis="columns", how="all").replace(np.nan, "")
        if tmp.shape[1] != len(cols):
            for elem in cols:
                for col in tmp.columns:
                    if elem == col:
                        break
                else:
                    print(f'{elem} is not in the columns anymore because the column was empty.')

        return tmp

    if cols:
        return tmp_what_to_do_with_cols(df_consolidated,
                           according_to,
                           cols)
    else:
        cols = df_consolidated.columns
        return tmp_what_to_do_with_cols(df_consolidated,
                           according_to,
                           cols)

# ---------------------- Demarches_PCAET_V2_PEC_SEQ -------------
"""
Les fichiers « Démarches PCAET [V1 ou V2] PEC SEQ » comprennent les informations
des fichiers ENTETE ainsi que les données et objectifs sur la consommation
d’énergie, les émissions de gaz à effet de serre, la vulnérabilité au
changement climatique et la séquestration carbone.
"""

def pec_ges(elem):
    """
    from elem, returns n1 and n2
    """
    n1, n2 = (elem.replace("PEC_GES","").split("_")[1:])
    return n1, n2

def pec_conso(elem):
    """
    from elem, returns n1 and n2
    """
    n1, n2 = (elem.replace("PEC_CONSO","").split("_")[1:])
    return n1, n2

def seq_(elem):
    """
    from elem, returns n1 and n2
    """
    n1 = (elem.replace("SEQ_","").split("_")[:])[0]
    n2 = "_".join(elem.replace("SEQ_","").split("_")[:])[1:]
    return n1,n2

def about_seq_secteur(seq_secteur):
    """
    Mapps n1 for SEQ
    """
    seq_secteur_dict = {
        "1":"Forêt",
        "2":"Terre_cultivées_et_prairies",
        "3":"Autres_sols",
    }

    for key in seq_secteur_dict:
        if seq_secteur == key:
            return seq_secteur_dict[key]

def interm_new_mapping(
                       elem, new_mapps,
                       pec__ges=False,
                       pec__conso=False,
                       seq=False):
    if pec__ges == True:
        n1, n2 = pec_ges(elem)
        n1 = about_secteur(n1)
        n2 = about_periode(n2)
        new_mapps[elem] = "PEC_GES_" +n1+"_"+n2+ "(en TeqCO2)"

    elif pec__conso == True:
        n1, n2 = pec_conso(elem)
        n1 = about_secteur(n1)
        n2 = about_periode(n2)
        new_mapps[elem] = "PEC_CONSO_" +n1+"_"+n2+ "(en Gwh)"

    elif seq == True:
        n1, n2 = seq_(elem)
        new_mapps[elem] = "SEQ_" + about_seq_secteur(n1) + n2

    return new_mapps

def new_mapping(larochelle):
    new_mapps = {}
    pecges = []
    pecconso = []
    seq = []

    for i, elem in enumerate(larochelle.index):
        if "PEC_GES" in elem:
            try:
                new_mapps = interm_new_mapping(elem, new_mapps, pec__ges= True)
            except TypeError:
                next
        if elem.startswith("PEC_GES"):
            pecges.append(larochelle.iloc[i,:1].values[0])
        else: pecges.append(False)

        if "PEC_CONSO" in elem:
            new_mapps = interm_new_mapping(elem, new_mapps, pec__conso=True)
        if elem.startswith("PEC_CONSO"):
            pecconso.append(larochelle.iloc[i,:1].values[0])
        else: pecconso.append(False)

        try:
            if "SEQ" in elem:
                n1,n2 = seq_(elem)
                new_mapps[elem] = "SEQ_" + about_seq_secteur(n1) + n2
            if elem.startswith("SEQ"):
                seq.append(larochelle.iloc[i,:1].values[0])
            else: seq.append(False)
        except TypeError:
            seq.append(False)

    mapping_index = [new_mapps.get(element, element) for element in list(larochelle.index)]
    larochelle.index = mapping_index

    for elem in to_be_mapped:
        larochelle[elem] = for_specific_year_or_sector(elem, larochelle)

    # Profil Energie Climat - émissions GES
    larochelle["PEC_GES"] = pecges

    # Profil Energie Climat - Consommation énergétique
    larochelle["PEC_CONSO"] = pecconso

    # Profil Energie Climat - Vulnérabilité

    # Profil Energie Climat - Séquestration
    larochelle["SEQ"] = seq

    # Profil Energie Climat - Objectifs de renforcements de la séquestration


    return larochelle

# ---------------------- Demarches_PCAET_V2_ENR -----------------
"""
Les fichiers « Démarches PCAET [V1 ou V2] ENR » comprennent les informations
des fichiers ENTETE ainsi que les données et objectifs sur la production et la
consommation d’énergie renouvelable, les énergies de récupération, le stockage
énergétique et les évolutions des réseaux.
"""

def diag_annee_compta(elem):
    """
    from elem, returns n1 and n2
    """
    n1 = (elem.replace("ENR_","").split("_")[0])
    n2 = "_".join(elem.replace("ENR_","").split("_")[1:])
    return n1, n2

def enr_production(elem):
    """
    from elem, returns n1 and n2
    """
    interm = (elem.replace("ENR_","").replace("_Production",""))
    n1 = interm.split("_")[0]
    n2 = "_".join(interm.split("_")[1:])
    return n1, n2

def enr_consommation(elem):
    """
    from elem, returns n1 and n2
    """
    interm = (elem.replace("ENR_","").replace("_Consommation",""))
    n1 = interm.split("_")[0]
    n2 = "_".join(interm.split("_")[1:])
    return n1, n2

def enr_valo_recup(elem):
    """
    from elem, returns n1 and n2
    """
    n2 = elem.replace("ENR_valorisation_recuperation_","")
    return n2

def enr_valo_stockage(elem):
    """
    from elem, returns n1 and n2
    """
    n2 = elem.replace("ENR_valorisation_stockage_","")
    return n2

def about_liste_codes_filieres(filiere):
    """
    Mapps n1 for diag_annee_compta
    """
    filiere_dict = {
        "1":"Eolien_terrestre",
        "2":"Solaire_photovoltaïque",
        "3":"Solaire_thermodynamique",
        "4":"Hydraulique",
        "5":"Biomasse_solide",
        "6":"Biogaz",
        "7":"Géothermie",
        "8":"Biomasse_solide",
        "9":"Pompes_à_chaleur",
        "10":"Géothermie",
        "11":"Solaire_thermique",
        "12":"Biogaz",
        "13":"Biométhane(en GWh)",
        "14":"Biocarburants(en GWh)"
    }

    for key in filiere_dict:
        if filiere == key:
            return filiere_dict[key]

def code_type_filiere(type):
    """
    Mapps n2 for diag_annee_compta
    """
    type_dict = {
        "1":"Electricité(en GWh)",
        "2":"Chaleur(en GWh)",
        "3":"Biométhane(en GWh)",
        "4":"Biocarburants(en GWh)"
    }

    for key in type_dict:
        if type == key:
            return type_dict[key]

def code_type_filiere_according_to_n1(n1,n2):
    if n1 == "1":
        n2 = "1"
        return n2
    elif n1 == "2":
        n2 = "1"
        return n2
    elif n1 == "3":
        n2 = "1"
        return n2
    elif n1 == "4":
        n2 = "1"
        return n2
    elif n1 == "5":
        n2 = "1"
        return n2
    elif n1 == "6":
        n2 = "1"
        return n2
    elif n1 == "7":
        n2 = "1"
        return n2
    elif n1 == "8":
        n2 = "2"
        return n2
    elif n1 == "9":
        n2 = "2"
        return n2
    elif n1 == "10":
        n2 = "2"
        return n2
    elif n1 == "11":
        n2 = "2"
        return n2
    elif n1 == "12":
        n2 = "2"
        return n2
    elif n1 == "13":
        n2 = "3"
        return n2
    elif n1 == "14":
        n2 = "4"
        return n2

def interm_new_mapping_ENR(
                       elem, new_mapps,
                       diag__compta=False,
                       production_=False,
                       consommation_ = False,
                       valorisation_recuperation = False,
                       valorisation_stockage = False,
                       ):
    if diag__compta == True:
        n1, n2 = diag_annee_compta(elem)
        n3 = code_type_filiere((code_type_filiere_according_to_n1(n1,n2)))
        n1 = about_liste_codes_filieres(n1)
        new_mapps[elem] = "ENR_" + n1 + "_" + n3 + "_" + n2
    if production_ == True:
        n1, n2 = enr_production(elem)
        n3 = code_type_filiere((code_type_filiere_according_to_n1(n1,n2)))
        n1 = about_liste_codes_filieres(n1)
        new_mapps[elem] = "ENR_" + n1 + "_" + n3 + about_periode(n2) + "_Production"
    if consommation_ == True:
        n1, n2 = enr_consommation(elem)
        n3 = code_type_filiere((code_type_filiere_according_to_n1(n1,n2)))
        n1 = about_liste_codes_filieres(n1)
        new_mapps[elem] = "ENR_" + n1 + "_" + n3 + about_periode(n2) + "_Consommation"
    if valorisation_recuperation == True:
        n2 = enr_valo_recup(elem)
        new_mapps[elem] = "ENR_valorisation_recuperation_" + about_periode(n2)
    if valorisation_stockage == True:
        n2 = enr_valo_stockage(elem)
        new_mapps[elem] = "ENR_valorisation_stockage_" + about_periode(n2)

    return new_mapps

def new_mapping_ENR(larochelle):
    new_mapps = {}
    diag_compta = []
    enr_prod = []
    enr_conso = []
    enr_valo_recup = []
    enr_valo_stock = []

    for i, elem in enumerate(larochelle.index):
        try:
            if elem.endswith("_Diag_Annee_Compta"):
                diag_compta.append(larochelle.iloc[i,:1].values[0])
                new_mapps = interm_new_mapping_ENR(elem, new_mapps, diag__compta= True)
            else: diag_compta.append(False)

            if elem.endswith("Production"):
                enr_prod.append(larochelle.iloc[i,:1].values[0])
                new_mapps = interm_new_mapping_ENR(elem, new_mapps, production_=True)
            else: enr_prod.append(False)

            if elem.endswith("Consommation"):
                enr_conso.append(larochelle.iloc[i,:1].values[0])
                new_mapps = interm_new_mapping_ENR(elem, new_mapps, consommation_=True)
            else: enr_conso.append(False)

            if elem.startswith("ENR_valorisation_recuperation"):
                enr_valo_recup.append(larochelle.iloc[i,:1].values[0])
                new_mapps = interm_new_mapping_ENR(elem, new_mapps, valorisation_recuperation=True)
            else: enr_valo_recup.append(False)

            if elem.startswith("ENR_valorisation_stockage"):
                enr_valo_stock.append(larochelle.iloc[i,:1].values[0])
                new_mapps = interm_new_mapping_ENR(elem, new_mapps, valorisation_stockage=True)
            else: enr_valo_stock.append(False)

        except:
            next

    mapping_index = [new_mapps.get(element, element) for element in list(larochelle.index)]
    larochelle.index = mapping_index

    for elem in to_be_mapped:
        larochelle[elem] = for_specific_year_or_sector(elem, larochelle)

    # ENR _ Diag Année
    larochelle["Diag_Annee_Compta"] = diag_compta

    # ENR _ Production
    larochelle["Production"] = enr_prod

    # ENR _ Consommation
    larochelle["Consommation"] = enr_conso

    # ENR _ Valorisation_Recupération
    larochelle["valorisation_recuperation"] = enr_valo_recup

    # ENR _ Valorisation_Stockage
    larochelle["valorisation_stockage"] = enr_valo_stock

    return larochelle

# ---------------------- Demarches_PCAET_V2_Polluant ------------
"""
Les fichiers « Démarches PCAET [V1 ou V2] POLLUANT » comprennent les
informations des fichiers ENTETE ainsi que les données et objectifs sur les
émissions de polluants atmosphériques.
"""

def pol_generic(elem):
    """
    """
    secteur, periode, polluant = elem.replace("POL_","").split("_")
    return secteur, periode, polluant

def pol_diag_annee(elem):
    """
    """
    polluant = elem.replace("POL_","").replace("_Diag_Annee_Compta","").split("_")[0]
    return polluant

def pol_total(elem):
    """
    """
    polluant, periode = elem.replace("TOTAL_POL__","").split("_")
    return polluant, periode

def about_polluant(polluant):
    polluant_dict = {
        "1": "PM10",
        "2": "PM2.5",
        "3": "Oxydes_d_azote",
        "4": "Dioxyde_de_soufre",
        "5": "COV",
        "6": "NH3",
    }

    for key in polluant_dict:
        if polluant == key:
            return polluant_dict[key]

def interm_new_mapping_POL(
                       elem,
                       new_mapps,
                       polluant_generic=False,
                       polluant_diag_annee=False,
                       polluant_total=False,
                       ):
    """
    """
    if polluant_generic == True:
        secteur, periode, polluant = pol_generic(elem)
        new_mapps[elem] = "POL_" + about_secteur(secteur) + "_" + about_periode(periode) + "_" + about_polluant(polluant)

    if polluant_diag_annee == True:
        polluant = pol_diag_annee(elem)
        new_mapps[elem] = "POL_" + about_polluant(polluant) + "_Diag_Annee_Compta"

    if polluant_total == True:
        polluant, periode = pol_total(elem)
        new_mapps[elem] = "TOTAL_POL__" + about_polluant(polluant) + "_" + about_periode(periode)

    return new_mapps

def new_mapping_POL(larochelle):
    new_mapps = {}
    pol_gen = []
    pol_diag_an = []
    total_pol = []

    for i,elem in enumerate(larochelle.index):
        try:
            if not elem.endswith("compta") and not elem.endswith("Compta") and not elem.endswith("ommentaire") and elem.startswith("POL"):
                pol_gen.append(larochelle.iloc[i,:1].values[0])
                new_mapps = interm_new_mapping_POL(elem, new_mapps, polluant_generic= True)
            else: pol_gen.append(False)

            if elem.endswith("Diag_Annee_Compta"):
                pol_diag_an.append(larochelle.iloc[i,:1].values[0])
                new_mapps = interm_new_mapping_POL(elem, new_mapps, polluant_diag_annee=True)

            else: pol_diag_an.append(False)

            if elem.startswith("TOTAL_POL"):
                total_pol.append(larochelle.iloc[i,:1].values[0])
                new_mapps = interm_new_mapping_POL(elem, new_mapps, polluant_total=True)

            else: total_pol.append(False)

        except TypeError:
            next

    mapping_index = [new_mapps.get(element, element) for element in list(larochelle.index)]
    larochelle.index = mapping_index

    for elem in to_be_mapped:
        larochelle[elem] = for_specific_year_or_sector(elem, larochelle)

    # Polluant generic
    larochelle["Polluant_generic"] = pol_gen

    # Polluant diag année
    larochelle["Polluant_Diag_Annee"] = pol_diag_an

    # Polluant total
    larochelle["TOTAL_POL"] = total_pol

    return larochelle

# ---------------------- MERGE ALL ------------

def merge_all(local_authority_name="La_Rochelle",
            nb_of_lines=2,
            idx_of_local_authority=1,
            ):

    # PEC SEQ
    larochelle_pec_seq = load_data(csv="Demarches_PCAET_V2_PEC_SEQ.csv",
          nb_of_lines=nb_of_lines,
          idx_of_local_authority=idx_of_local_authority,
          local_authority_name=local_authority_name)
    larochelle_pec_seq = new_mapping(larochelle_pec_seq)

    # Demarches_PCAET_V2_ENR
    larochelle_enr = load_data("Demarches_PCAET_V2_enr.csv",
                            nb_of_lines=nb_of_lines,
                            idx_of_local_authority=idx_of_local_authority,
                            local_authority_name=local_authority_name)
    larochelle_enr = new_mapping_ENR(larochelle_enr)

    # Demarches_PCAET_V2_Polluant
    larochelle_pol = load_data("Demarches_PCAET_V2_Polluant.csv",
                            nb_of_lines=nb_of_lines,
                            idx_of_local_authority=idx_of_local_authority,
                            local_authority_name=local_authority_name)
    larochelle_pol = new_mapping_POL(larochelle_pol)

    # Merge all
    larochelle = pd.concat([larochelle_pec_seq,larochelle_enr, larochelle_pol])
    return larochelle
