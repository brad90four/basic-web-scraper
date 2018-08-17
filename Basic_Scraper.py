# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 20:00 2018
Basic Web Scraper
@author: Brad
"""

try:
    import requests
    from bs4 import BeautifulSoup
    import os
    import time
    import csv
    import pandas as pd
    import numpy as np
except ImportError:
    raise SystemExit("Please import requests, BeautifulSoup, os and time and try again.")

file_path = os.path.abspath(__file__)
project_directory = os.path.dirname(file_path)
scrape_folder = os.path.join(project_directory + "\scrape_data")
os.chdir(project_directory)

def scrape_info():
    """Gathers relevant web scraping data.
    
    Returns url, new_scrape_name and target_tag from input.
    """
    url = input("Enter url: ")
    new_scrape_name = input("Enter text file name: ")
    target_tag = input("What HTML tag are you looking for? : ")
    return url, new_scrape_name, target_tag


def basicscraper(url, new_scrape_name, target_tag):
    """Goes to url, takes text from target_tag, outputs text with new line \
    in new_scrape_name.txt.
    
    Note:
    If using on it's own, need to input arguments as strings. \
    e.g. basicscraper("url", "new_scrape_name", "target_tag")
    Keyword arguments:
    url -- the webpage to scrape
    new_scrape_name -- the text file output title
    target_tag -- the HTML tag to scrape the text for
    """
    page_data = requests.get(url)
    soup = BeautifulSoup(page_data.text, "lxml")
    for something in soup.find_all(target_tag):
        tag_text = something.text.strip()
        if not os.path.exists(scrape_folder):
            os.makedirs(project_directory + "\scrape_data")
            with open(os.path.join(scrape_folder, new_scrape_name + ".csv"), "a") as output:
                output.write(url + "|" + target_tag + "|" + time.strftime("%d%m%Y") + "|" + tag_text + "\n")
        os.chdir(scrape_folder)
        with open(new_scrape_name + ".csv", "a") as output:
            output.write(url + "|" + target_tag + "|" + time.strftime("%d%m%Y") + "|" + tag_text + "\n")
        os.chdir(project_directory)


def scrape_away(url=None, new_scrape_name=None, target_tag=None):
    """If arguments are None, calls scrape_info. Otherwise passes arguments
    to basicscraper."""
    if url is None and new_scrape_name is None and target_tag is None:
        url, new_scrape_name, target_tag = scrape_info()
        basicscraper(url, new_scrape_name, target_tag)
    else:
        basicscraper(url, new_scrape_name, target_tag)
