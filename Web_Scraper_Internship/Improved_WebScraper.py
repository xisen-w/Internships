import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Step 1: Set URL, Data, and Driver
url = "https://www.cancerresearchuk.org/about-cancer/find-a-clinical-trial/clinical-trials-search?search_api_aggregation_1=breast&f%5B0%5D=field_trial_status%3A4386"
driver_path = "path/to/chromedriver"
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(driver_path, options=options)
driver.get(url)

# Step 2: Navigate through Pagination
while True:
    try:
        next_button = driver.find_element(By.XPATH, "//a[@title='Go to next page']")
        trials = driver.find_elements(By.XPATH, "//a[@class='link-item']")
        trial_urls = [trial.get_attribute("href") for trial in trials]
        print(trial_urls)
    except Exception:
        break

    # Step 3: Click into each trial URL and extract data fields
    for trial_url in trial_urls:
        driver.get(trial_url)
        data = {}
        data["Status"] = driver.find_element_by_xpath("//label[contains(text(),'Status:')]/following-sibling::div").text
        data["Supported By"] = driver.find_element_by_xpath("//label[contains(text(),'Sponsor:') or contains(text(),'Sponsorship:')]/following-sibling::div").text
        data["Phase"] = driver.find_element_by_xpath("//label[contains(text(),'Phase:')]/following-sibling::div").text
        data["Name"] = driver.find_element_by_tag_name("h1").text
        data["Page URL"] = trial_url

        # Step 4: Save data into CSV
        with open("trials.csv", mode="a", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(data)

    if next_button and next_button.is_enabled():
        next_button.click()
    else:
        break

# Close the Driver at the end of program
driver.close()