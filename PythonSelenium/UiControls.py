import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
     if checkbox.get_attribute("value") == "option2":
         checkbox.click()
         time.sleep(2)
         assert checkbox.is_selected()
         break

radios = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radios[1].click()
time.sleep(1)
assert radios[1].is_selected()

# hide = driver.find_element(By.ID, "hide-textbox")
# hide.click()
# time.sleep(1)
# #time.sleep(1)
# show = driver.find_element(By.ID, "show-textbox")
# show.click()
# time.sleep(1)
#
# if hide.click():
#     assert hide.is_displayed()
# if show.click():
#     assert show.is_displayed()

assert driver.find_element(By.ID, "displayed-text").is_displayed()
time.sleep(1)
driver.find_element(By.ID, "hide-textbox").click()
time.sleep(1)
assert not driver.find_element(By.ID, "displayed-text").is_displayed()

driver.close()