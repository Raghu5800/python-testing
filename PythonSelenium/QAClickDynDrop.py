import time

import driver
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

# Dynamic Dropdown
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)

countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    print(country.text)
    if country.text == "India":
        print("country is:", country.text)
        country.click()
        time.sleep(2)
        break

assert (driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India")






