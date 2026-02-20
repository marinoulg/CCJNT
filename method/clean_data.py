import os
from params import *

def clean_data_dir():
    for elem in os.listdir(LOCAL_DATA_PATH):
        if "emarche" not in elem:
            os.remove(os.path.join(LOCAL_DATA_PATH,elem))

if __name__ == "__main__":
    clean_data_dir()
