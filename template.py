import os, sys 
from pathlib import Path
import logging

logging.basicConfig(filename= "template_logs.txt",level= logging.DEBUG, format = '[(%asctime)s] : %(message)s:')


project_name = input(str("provide your project name here :"))

if project_name == '':

    raise "we need a prject name to conitnue"

if project_name != "":

    list_of_files = [
        ".github/workflows/.gitkeep",
        "data/.gitkeep",
        "docs/.gitkeep",
        f"{project_name}/__init__.py",
        f"{project_name}/components/__init__.py",
        f"{project_name}/components/data_ingestion.py",
        f"{project_name}/components/data_validation.py",
        f"{project_name}/components/model_trainer.py",
        f"{project_name}/components/model_pusher.py",

        f"{project_name}/s3/__init__.py",
        f"{project_name}/s3/s3_operations.py",

        f"{project_name}/constant/__init__.py",
        f"{project_name}/constant/training_pipeline/__init__.py",
        f"{project_name}/constant/application.py",

        f"{project_name}/entity/__init__.py",
        f"{project_name}/entity/artifacts.py",
        f"{project_name}/entity/config.py",

        f"{project_name}/exception/__init__.py",
        f"{project_name}/logger/__init__.py",

        
        f"{project_name}/pipeline/__init__.py",
        f"{project_name}/pipeline/training_pipeline.py",

        f"{project_name}/utils/__init__.py",
        f"{project_name}/utils/utilities.py",

        "template/index.html",
        ".dockerignore",
        ".gitignore",
        "app.py",
        "Dockerfile",
        "requirements.txt",
        "setup.py",
        "main.py"


    ]


for filepath in list_of_files:
    filepath = Path(filepath) # auttomatically detect machine and give / \ between path

    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok= True)
        logging.info(f"creating directory : {filedir} for the file {filename}")

    if(not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"creating the empty file :{filename}")

        


