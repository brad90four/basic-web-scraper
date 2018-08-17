try:
    import os
    import time
    import csv
    import pandas as pd
    import numpy as np
    import matplotlib as plt
    import glob
except ImportError:
    raise SystemExit("Please import modules and try again.")

file_path = os.path.abspath(__file__)
project_directory = os.path.dirname(file_path)
scrape_folder = os.path.join(project_directory + "\scrape_data")
os.chdir(project_directory)

def latest_scrape():
    os.chdir(scrape_folder)
    scrape_folder_files = glob.glob("*.csv")
    global latest_scrape_file
    latest_scrape_file = max(scrape_folder_files, key=os.path.getctime)

latest_scrape()

scrape_dataframe = pd.read_csv(latest_scrape_file, delimiter="|", encoding="cp1252",
                               names=["URL", "HTML Tag", "Date", "Text"])