import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
driver.maximize_window()

cont = driver.find_element(By.ID,"login-continue-btn")
driver.save_screenshot("yatra_loginPass.png" )
time.sleep(2)
cont.click()
time.sleep(2)
driver.save_screenshot("yatra_signin1Er.png")
driver.get_screenshot_as_file("/Users/raghu/Python_Projects/PythonTesting/PythonSelenium/test1.png")
time.sleep(2)
driver.quit()