#Webscraper

#imports 
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import time 

# set up driver

PATH = "/Users/wangxiang/Desktop/Web_Scraper_Internship/chromedriver"
url = "https://www.cancerresearchuk.org/about-cancer/find-a-clinical-trial/trials-by-cancer-type"

#define our driver
driver = webdriver.Chrome(PATH)
driver.get(url)

# find cancer type elements
cancer_type_elements = driver.find_elements(By.CSS_SELECTOR, "div.form-item-cancer-type > label")

# extract cancer types
cancer_types = []
for cancer_type_element in cancer_type_elements:
    cancer_types.append(cancer_type_element.text)

# print list of cancer types
print(cancer_types)

# close driver
driver.quit()

#setups
PATH = "/Users/wangxiang/Desktop/Web_Scraper_Internship/chromedriver"
url = "https://www.cancerresearchuk.org/about-cancer/find-a-clinical-trial"

#define our driver
driver = webdriver.Chrome(PATH)
driver.get(url)

#Find all cancer types
try:
    cancer_types = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "item-list"))
    )
    print(f"Found {len(cancer_types)} cancer types")
except:
    driver.quit()

#Loop through each cancer type
for cancer_type in cancer_types:
    #Extract the cancer type text and click the checkbox
    type_text = cancer_type.text
    cancer_type.click()
    
    #Click search button
    search = driver.find_element(By.ID,'edit-submit-find-a-clinical-trial')  
    search.click()

    time.sleep(10)

    #Loop through each clinical trial URL in the current cancer type page
    try:
        trials = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.search-result > h3 > a"))
        )
        print(f"Found {len(trials)} trials for {type_text}")
    except:
        driver.quit()

    for trial in trials:
        trial_name = trial.text
        trial_url = trial.get_attribute("href")
        driver.get(trial_url)

        #Scrape the trial information
        try:
            trial_type = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.trial-summary-detail > span"))
            ).text
            institutions = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.trial-summary-detail + div > span"))
            ).text
            trial_status = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.trial-summary-detail + div + div > span"))
            ).text
            trial_phase = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.trial-summary-detail + div + div + div > span"))
            ).text
            print(f"Trial Name: {trial_name}")
            print(f"Trial Type: {trial_type}")
            print(f"Institutions: {institutions}")
            print(f"Trial Status: {trial_status}")
            print(f"Trial Phase: {trial_phase}")
        except:
            print(f"Error scraping trial information for {trial_name}")
        
        #Go back to the search results page
        driver.back()

    #Clear the cancer type checkbox to prepare for the next iteration
    cancer_type.click()

driver.quit()

print("Done scraping clinical trials")

