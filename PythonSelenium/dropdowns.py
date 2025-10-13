import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://practice.expandtesting.com/dropdown")
driver.maximize_window()

if (driver.find_element(By.XPATH, "//h2[normalize-space()='Simple dropdown']")).text == "Simple dropdown":
    sel = Select(driver.find_element(By.ID, "dropdown"))
    sel.select_by_visible_text("Option 1")
    time.sleep(3)
    sel.select_by_visible_text("Option 2")
    time.sleep(3)

if driver.find_element(By.XPATH, "//h2[normalize-space()='Select your date of birth']").text == "Select your date of birth" and driver.find_element(By.XPATH, "//label[normalize-space()='Elements per Page:']").text == "Elements per Page:":
    sel1 = Select(driver.find_element(By.XPATH,"//select[@id='elementsPerPageSelect']"))
    sel1.select_by_value("20")
    time.sleep(2)

try:
    if driver.find_element(By.XPATH, "//h2[normalize-space()='Country selection']").text == "Country selection":
        sel2 = Select(driver.find_element(By.ID, "country"))
        sel2.select_by_visible_text("India")  # use visible text, not value
        time.sleep(2)
except Exception as e:
    print("Country selection failed:", e)
    driver.quit()


driver.close()

