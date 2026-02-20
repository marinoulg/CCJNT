from method.methode_ecologiedatagouvfr import *
from method.params import *

import os
import pandas as pd

cols_of_interest = [
    "Description_rapide",
    "Collectivités porteuses",
    "Elu_referent",
    "Commentaire_statut",
]
# same for all

def find_indexes_for_community_per_dataset(data_path, community):
    data = pd.read_csv(data_path,
                   sep=";",
                   index_col="Id")

    indexes = set()
    for idx in data.index:
        for col in cols_of_interest:
            try:
                if community in data.loc[idx,col].lower():
                    indexes.add(idx)
            except AttributeError:
                next

    indexes = list(indexes)
    return data, indexes

def return_temp_df_consolidated_for_one_community(data_path, community):
    data, indexes = find_indexes_for_community_per_dataset(data_path, community)

    df_consolidated = pd.DataFrame()
    for i, index in enumerate(indexes):
        if i == 0:
            df_consolidated = pd.DataFrame([data.loc[index,:]],
                                            columns=data.columns,
                                            )
        else:
            new_df = pd.DataFrame([data.loc[index,:]],
                                    columns=data.columns,
                                    )
            df_consolidated = pd.concat([df_consolidated,new_df], axis=0)
    return df_consolidated


def get_df_consolidated_for_all_communities_one_dataset(communities,data_path):
    df = pd.DataFrame()
    for i, community in enumerate(communities):
        community = community.lower()
        tmp_df = return_temp_df_consolidated_for_one_community(data_path, community)

        if i == 0:
            df = tmp_df
        else:
            new_df = tmp_df
            df = pd.concat([df,new_df], axis=0)

    return df

def save_csv(data_path,
             communities=COMMUNITIES_WIP):

    # Create WIP directory if doesn't exist
    os.makedirs(os.path.join(PCAET_DIR,"WIP"), exist_ok=True)

    df = get_df_consolidated_for_all_communities_one_dataset(communities=communities,
                                                             data_path=data_path)

    # Save csv to WIP directory
    df.to_csv(os.path.join(PCAET_DIR,"WIP",f"{data_path.split("/")[-1]}"),
              sep=";",
              index=False)

def save_all_csvs(which_version_of_PCAET_DATA=PCAET_V2_DATA,
                  communities=COMMUNITIES_WIP
                  ):
    for i in range(len(os.listdir(which_version_of_PCAET_DATA))):
        data_path = os.path.join(which_version_of_PCAET_DATA, os.listdir(which_version_of_PCAET_DATA)[i])
        save_csv(data_path=data_path, communities=communities)

if __name__ == "__main__":
    save_all_csvs(PCAET_V2_DATA, COMMUNITIES_WIP)
    save_all_csvs(PCAET_V1_DATA, COMMUNITIES_WIP)
