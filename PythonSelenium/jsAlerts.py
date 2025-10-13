import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Raghuu")
driver.find_element(By.ID, "alertbtn").click()
time.sleep(2)
alert = driver.switch_to.alert
alertTxt = alert.text
print(alertTxt)
assert alertTxt == "Hello Raghuu, share this practice page and share your knowledge"
alert.accept()

driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Raghuu")
driver.find_element(By.ID, "confirmbtn").click()
time.sleep(2)
alert1 = driver.switch_to.alert
alertTxt1 = alert1.text
print(alertTxt1)
assert alertTxt1 == "Hello Raghuu, Are you sure you want to confirm?"
alert1.accept()
time.sleep(2)

driver.close()