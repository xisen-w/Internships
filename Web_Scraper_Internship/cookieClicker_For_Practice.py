from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import time 

#setups
url = "https://orteil.dashnet.org/cookieclicker/"

#define our driver
driver = webdriver.Chrome()
driver.get(url)

#Waiting for the driver to upload 
time.sleep(5)
wait = WebDriverWait(driver, 10)
#consent_button = driver.find_element(By.CLASS_NAME,"fc-footer-buttons")
#real_consent_button = consent_button.find_element(By.TAG_NAME,"button")
lang = driver.find_element(By.ID,"langSelect-EN")
lang.click() 

#consent_button = wait.until(EC.presence_of_element_located((By.TAG_NAME, "button")))
#Go over the consent & Choose language stuff
#consent_button.click()

#access to cookies & cookie accounts
cookie = driver.find_element(By.ID,"bigCookie")
cookie_count = driver.find_element(By.ID,"cookies")
items = [driver.find_element(By.ID,"productPrice" + str(i)) for i in range (2,-1,-1)]

print("Let's get started")

#action chain here

for i in range(5000): #press the cookie 50000
    actions = ActionChains(driver)
    actions.click(cookie)
    actions.perform()
    scount = cookie_count.text.split(" ")[0]
    count = int(scount)
    for item in items:
        value = int(item.text)
        if count < 50:
            if value <= count:
                upgrade_actions = ActionChains(driver)
                upgrade_actions.move_to_element(item)
                upgrade_actions.click()
                upgrade_actions.perform()
        elif 100 < count < 150:
            if value <= count:
                upgrade_actions = ActionChains(driver)
                upgrade_actions.move_to_element(item)
                upgrade_actions.click()
                upgrade_actions.perform()
        elif count > 200:
            if value <= count:
                upgrade_actions = ActionChains(driver)
                upgrade_actions.move_to_element(item)
                upgrade_actions.click()
                upgrade_actions.perform()

            



