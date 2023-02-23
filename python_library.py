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

## Working With Timestamps
    # import time
    # time.time()
    # def send_emails():
        # for i in range(10000):
            # pass

## Working With DateTimes 
    # import datetime
    # from datetime import datetime
    # datetime.now()
    # datetime.strptime("2018/01/01", "%Y/%m/%d")

## Time Deltas
    # from datetime import datetime, timedelta

## Generation Random Values
    # check back for random passwords
    # import random
        # between 0 and 1
    # random.randint(1, 10)
        # can random between two numbers
    # random.choice({1, 2, 3, 4}, k=2)
        # randomly chooses items from array or string
        # k= is how many items to get

## Opening the Browser
    # import webbrowser
    # webbrowser.open("http://website.com")

## Sending Emails
    # from email.mime.multipart import MIMEMultipart
    # from email.mime.text import MIMEText
    # import smtplib

## Templates
    # use html

## Command-line Arguments
    # import sys
    # sys.argv

## Running External Programs
    # import subprocess