import os
from params import *

def clean_data_dir():
    for elem in os.listdir(PATH_DATA_WIP):
        os.remove(os.path.join(PATH_DATA_WIP,elem))
    os.removedirs(PATH_DATA_WIP)

if __name__ == "__main__":
    clean_data_dir()
