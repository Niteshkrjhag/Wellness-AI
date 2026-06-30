import os
from pathlib import Path
import logging

# Configure logging so that messages are displayed with timestamps
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s]: %(message)s:'
)

# List of files and folders that should be created
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",             # Used for packaging the project
    "app.py",
    "research/trails.ipynb" # Jupyter notebook for experiments

]

# Loop through each path in the list
for filepath in list_of_files:

    # Convert string path into a Path object
    # Path handles Windows (\) and Mac/Linux (/) automatically
    filepath = Path(filepath)

    # Split path into:
    # filedir  -> directory path
    # filename -> actual file name
    #
    # Example:
    # "src/helper.py"
    # filedir  = "src"
    # filename = "helper.py"
    filedir, filename = os.path.split(filepath)

    # checks wheather a directory exists in the path or not
    if filedir != "":

        # Create the directory if it does not already exist
        # exist_ok=True prevents errors if directory already exists
        os.makedirs(filedir, exist_ok=True)

        logging.info(
            f"Creating directory: {filedir} for the file: {filename}"
        )

    # Check whether:
    # 1. File does not exist
    # OR
    # 2. File exists but is empty (size = 0 bytes)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):

        # Create an empty file
        with open(filepath, "w") as f:
            pass

        logging.info(f"Creating empty file: {filepath}")

    else:
        # File already exists and contains data
        logging.info(f"{filename} already exists")