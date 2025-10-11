import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/client/#/auth/login")
driver.maximize_window()

driver.find_element(By.ID, "userEmail").send_keys("test1@gmail.com")
driver.find_element(By.ID, "userPassword").send_keys("Dummy1")
driver.find_element(By.CSS_SELECTOR, "input[type=submit]").click()
time.sleep(1)

driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter your email address']").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "#userPassword").send_keys("test1")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("test1")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()



time.sleep(3)
driver.close()
