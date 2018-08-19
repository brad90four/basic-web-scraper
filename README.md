# basic-web-scraper
First Basic Web Scraper with Python

Uses two different scripts, one to create a .csv file with the scrape data and another to create a bar plot based on the number of times a keyword is mentioned in the Text column of the web scrape. 

First run Basic_Scraper.py (call scrape_away()) and give the url to scrape, HTML tag to take the text from and the .csv filename you want to create. 

This will create a folder where the script is downloaded to in order to hold all of the scrape.csv files.

Second run Scrape_Reader.py (call keyword_plot()) and give the keyword. This will open the most recent .csv file and look for the keyword in the text column, will plot the date and url vs the total amount of times the keyword is called. 

## Example Figure
![trump_scrape](https://user-images.githubusercontent.com/42116429/44309717-d93fe580-a398-11e8-9320-555bb8474311.png)

