## Python Standard Library
    # Files, SQlite, Date/time, Random values

## Working with Paths
    # from pathlib import Path  
    # Path("/ust/local/bin")
    # multiple
        # Path() / "ecommerce" / "__init__.py"
    # Path.home() = to return home

## Working with Directories
    # iterdir 
        # will show where the file is located
        # loop will show what is in the folder
    # [p for p in path.iterdir() if p.is_dir()]

## Working with Files
    #path.unlink() = will uplink files
    # to print readable time
        # from time import ctime
            # ctime(path.start().st_ctime)

## Working with Zip Files
    # from zipfile import ZipFile

## Working with CSV Files
    # import csv
    # with open("data.csv", "w") as file:
        # writer = csv.writer(file)
        # reader = csv.reader(file) 
            # need to remove the w from with open

## Working with Json Files
    # import json
    # movies = [{"id"}]
    # data = json.dumps(movies)

## Working with SQLite Database
    # import sqlite3 
    # import json
    # from pathlib import Path
