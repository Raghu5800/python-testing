import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
driver.implicitly_wait(7)

new_sorted_list = []
driver.find_element(By.CSS_SELECTOR, "th:nth-child(1)").click()
time.sleep(2)

browser_val = driver.find_elements(By.XPATH, "//tr/td[1]")
for b in browser_val:
    new_sorted_list.append(b.text)

browser_sorted_val = new_sorted_list.copy()

new_sorted_list.sort()

assert browser_sorted_val == new_sorted_list, "Sorted list does not match"
time.sleep(1)
driver.quit()




