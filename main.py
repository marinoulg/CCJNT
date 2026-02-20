from method.methode_ecologiedatagouvfr import *
from pptx_dir.presentation import main_presentation
print(COMMUNITIES)

def main(communities):
    # Create consolidated csv for each community
    for community in communities:
        community_df = merge_all(local_authority_name=community,
                nb_of_lines=2,
                idx_of_local_authority=communities[community]["idx_of_local_authority"])
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
        main_presentation(community_df.columns[0].lower())

if __name__ == "__main__":
    main(COMMUNITIES)
