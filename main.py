from method.methode_ecologiedatagouvfr import *
from pptx_dir.presentation import main_presentation
print(COMMUNITIES)

# def main(communities,
#     # communities_WIP,
#          v1=False,
#          v2=True):

#     # # UPDATE communities
#     # communities = {}
#     # for community in communities_WIP:
#     #     print(community)
#     #     communities[community] = {"PATH": os.path.join(LOCAL_DATA_PATH,
#     #                                                 f"{community.lower().replace(" ","_")}.csv")
#     #                             }

#     # Create consolidated csv for each community
#     for community in communities:
#         community_df = merge_all(local_authority_name=community,
#                 nb_of_lines=None,
#                 idx_of_local_authority=None)
#         community_df.to_csv(path_or_buf=os.path.join(LOCAL_DATA_PATH,f"{community.lower()}.csv"), sep=';')
#         print(f"{community} csv done.")

#     # Charge the csv for each community and get the outputs, which in turn lead to the presentations
#     """
#     Verify what to do here, because not dynamic
#     if I add a new community_name in ```params.py```
#     """
#     for community in communities:
#         path_csv = (COMMUNITIES[community]["PATH"])
#         community_df = pd.read_csv(path_csv, sep=";").rename(columns={"Unnamed: 0":"index"}).set_index("index")

#         # Get outputs
#         get_outputs(community_df,
#                     steps=steps,
#                     # print_=True
#                     )
#         print(f"Ouputs created for {community_df.columns[0]}.")

#         # Create presentation in pptx format
#         main_presentation(community_df.columns[0].lower(),v1=v1, v2=v2)

# if __name__ == "__main__":
#     main(communities=COMMUNITIES,v2=True)

# from method.methode_ecologiedatagouvfr import *
# from pptx_dir.presentation import main_presentation
# print(COMMUNITIES)


# ---------------- what i had before ----------------
def main(communities,
         v1=False,
         v2=True):
    # Create consolidated csv for each community
    for community in communities:
        community_df = merge_all(local_authority_name=community,
                # nb_of_lines=2,
                # idx_of_local_authority=communities[community]["idx_of_local_authority"]
                )
        community_df.to_csv(path_or_buf=os.path.join(LOCAL_DATA_PATH,f"{community.lower()}.csv"), sep=';')
        print(f"{community} csv done.")

    # Charge the csv for each community and get the outputs, which in turn lead to the presentations
    for community in communities:
        path_csv = (COMMUNITIES[community]["PATH"])
        community_df = pd.read_csv(path_csv, sep=";").rename(columns={"Unnamed: 0":"index"}).set_index("index")

        # Get outputs
        get_outputs(community_df,
                    steps=steps,
                    # print_=True
                    )
        print(f"Ouputs created for {community_df.columns[0]}.")

        # Create presentation in pptx format
        main_presentation(community_df.columns[0].lower(),v1=v1, v2=v2)

if __name__ == "__main__":
    main(COMMUNITIES)
