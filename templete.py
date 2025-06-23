import os
from pathlib import Path
import logging

# Logging String
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')


project_name='DRPredictionModel'

list_of_files=[
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/componants/__init__.py",
    f"src/{project_name}/componants/data_ingestion.py",
    f"src/{project_name}/componants/data_transformation.py/",
    f"src/{project_name}/componants/model_trainer.py",
    f"src/{project_name}/componants/model_monitoring.py",
    f"src/{project_name}/pipelines/__init__.py"
    f"src/{project_name}/pipelines/training_pipelines.py",
    f"src/{project_name}/piplines/prediction_pipelines.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
    "research/trials.ipynb",
    "templates/index.html"
]

# Creating files and folders
for filepath in list_of_files: 
    filepath = Path(filepath)
    # separating the floders and file name
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")