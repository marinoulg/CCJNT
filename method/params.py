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

OUTPUTS_LAROCHELLE = os.path.join(LOCAL_PATH_OUTPUTS,"larochelle")
OUTPUTS_VALENCIENNES = os.path.join(LOCAL_PATH_OUTPUTS,"valenciennes")
