from bs4 import BeautifulSoup
import requests
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import time 

def find_basics():    
    #u'd better generate
    url_specific = "https://www.cancerresearchuk.org/about-cancer/find-a-clinical-trial/clinical-trials-search?populate=Breast%20cancer&f%5B0%5D=field_trial_status%3A4386"
    html_text = requests.get(url_specific).text #Get a url   
    #setups
    PATH = "/Users/wangxiang/Desktop/Web_Scraper_Internship/chromedriver"
    url = "https://www.cancerresearchuk.org/about-cancer/find-a-clinical-trial"
    #define our driver
    driver = webdriver.Chrome(PATH)
    driver.get(url);

    soup = BeautifulSoup(html_text,'lxml') #instantialize a single instance of BeautifulSoup
    trials = soup.findAll('td',class_='search-title') #make it text, replace matters less here
    for trial in trials:
        URL = trial.a['href'] #no need for td again
        trial_name = trial.text.replace("  "," ")
        print(f'URL: {URL}')
        print(f'Trial Name:{trial_name}')
        
if __name__ == '__main__':
    find_basics()
