try:
    import os
    import time
    import csv
    import pandas as pd
    import numpy as np
    import matplotlib as plt
    import glob
except ImportError:
    raise SystemExit("Please install modules and try again.")

#Setting paths to where the scrape.csv files are located
file_path = os.path.abspath(__file__)
project_directory = os.path.dirname(file_path)
scrape_folder = os.path.join(project_directory + "\scrape_data")
os.chdir(project_directory)

def latest_scrape():
    """latest_scrape function to return the most recent scrape.csv file.

    Returns scrape file path to be called by pandas dataframe scrape_dataframe
    """
    os.chdir(scrape_folder)
    scrape_folder_files = glob.glob("*.csv")
    global latest_scrape_file
    latest_scrape_file = max(scrape_folder_files, key=os.path.getctime)

latest_scrape()

"""Create pandas dataframe from most recent scrape.csv file. The encoding can change depending on windows version.
Common encoding is "cp1252", 'latin1', 'iso-8859-1'."""
scrape_dataframe = pd.read_csv(latest_scrape_file, delimiter="|", encoding="cp1252",
                               names=["URL", "HTML Tag", "Date", "Text"])

#Dataframe with na removed
cleaning_df = scrape_dataframe.dropna()

def keyword_plot(keyword=None):
    """A function to take a keyword in the Text column of the dataframe and plot the times it
    is mentioned vs time and url. Trying to add multiple series based on url.

    Arguments
    keyword -- string to investigate
    """
    if keyword is None:
        keyword=input("What string do you want to plot? : ")
        cleaning_df["Keyword Mentions"] = pd.np.where(cleaning_df.Text.str.contains(keyword), 1, 0)
        compare = cleaning_df[["Date", "URL", "Keyword Mentions"]]
        view_data = compare.groupby(["Date", "URL"])["Keyword Mentions"].sum()
        view_data.plot.bar()
    else:
        cleaning_df["Keyword Mentions"] = pd.np.where(cleaning_df.Text.str.contains(keyword), 1, 0)
        compare = cleaning_df[["Date", "URL", "Keyword Mentions"]]
        view_data = compare.groupby(["Date", "URL"])["Keyword Mentions"].sum()
        view_data.plot.bar()