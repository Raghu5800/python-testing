import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(1)

iff = driver.find_element(By.XPATH, "//legend[normalize-space()='iFrame Example']")
print(iff.text)
time.sleep(2)
assert iff.text == "iFrame Example", "Wrong text"
time.sleep(2)



driver.quit()


