import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
driver.maximize_window()

disp = driver.find_element(By.CSS_SELECTOR, "#myDIV").is_displayed()
print(disp)
time.sleep(2)

driver.find_element(By.XPATH, "//button[normalize-space()='Toggle Hide and Show']").click()
disp2 = driver.find_element(By.CSS_SELECTOR, "#myDIV").is_displayed()
print(disp2)











