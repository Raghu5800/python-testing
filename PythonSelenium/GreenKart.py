from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

vege = driver.find_element(By.CSS_SELECTOR, ".search-keyword")

vege.send_keys("Brocolli")


driver.close()