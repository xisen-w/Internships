from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Launch the browser and navigate to the page
driver = webdriver.Chrome()
driver.get("https://www.cancerresearchuk.org/about-cancer/find-a-clinical-trial/clinical-trials-search?populate=Brain%20%28and%20spinal%20cord%29%20tumours&f%5B0%5D=field_trial_status%3A4386")

# Wait for the page to load
time.sleep(5)

# Loop through each trial on the page
trials = driver.find_elements(By.CLASS_NAME,"views-row")
for trial in trials:
    # Click on the trial link to go to the detailed page
    trial_link = trial.find_element(By.TAG_NAME,"a")
    trial_url = trial_link.get_attribute("href")
    trial_link.click()
    
    # Wait for the detailed page to load
    time.sleep(5)
    
    # Extract the trial name, cancer type, and other useful information
    trial_name = driver.find_element(By.CSS_SELECTOR,"h1.page-title").text
    print(trial_name)
    #cancer_type = driver.find_element_by
