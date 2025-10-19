import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/select-menu")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "div[id='selectMenuContainer'] div[class='row'] div[class=' css-1wa3eu0-placeholder']").click()
time.sleep(2)