import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.execute_script("window.open('https://www.google.com/','_self');") # a js way of opening browser & end with semi-colon ;
driver.maximize_window()
time.sleep(5)

