from bs4 import BeautifulSoup
import requests

def find_basics():
    url = "https://www.cancerresearchuk.org/about-cancer/find-a-clinical-trial/clinical-trials-search?populate=Breast%20cancer&f%5B0%5D=field_trial_status%3A4386"
    html_text = requests.get(url).text #Get a url   
    soup = BeautifulSoup(html_text,'lxml') #instantialize a single instance of BeautifulSoup
    trials = soup.findAll('td',class_='search-title') #make it text, replace matters less here
    for trial in trials:
        URL = trial.a['href'] #no need for td again
        trial_name = trial.text.replace("  "," ")
        print(f'URL: {URL}')
        print(f'Trial Name:{trial_name}')
        
if __name__ == '__main__':
    find_basics()

    


