import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.yatra.com/hotels")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "div[class='SearchPanel_roomDetails__jjS6x'] div[class='SearchInputField_searchRegionInfo__R91xS']").click()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "body > main:nth-child(2) > div:nth-child(1) > main:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)").click()

driver.find_element(By.CSS_SELECTOR, "div[class='SelectRoom_selectorWrapper__OLC0A'] button[aria-label='1']").click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "div[class='SelectRoom_selectorGroup__mWhJB'] button[aria-label='0']").click()
time.sleep(2)

ax = driver.find_element(By.CSS_SELECTOR, "div[class='SelectRoom_selectorWrapper__OLC0A'] button[aria-label='1']")
print(ax.is_displayed())




