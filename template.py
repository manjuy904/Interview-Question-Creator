import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')


list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "app.py" 
]


# Integrating over each file in the list
for filepath in list_of_files:
    #converting filepath to a path object
    filepath = Path(filepath)
    #splitting the filepath into directory and filename
    filedir, filename = os.path.split(filepath)
    #print(filedir)
    #print(filename)
    
    #Checking if the file directory is not empty
    if filedir!="":
        #creating directory is does not exist
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for the files {filename}")
    
    #Checking if the file does not exist or is empty    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        #creating an empty file if it does not exist or empty
        with open(filepath, "w") as f:
            pass
        #logging the creation of empty file
        logging.info(f"Creating empty file : {filepath}")
        
    else:
        logging.info(f"{filename} is already exists")