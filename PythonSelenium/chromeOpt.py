import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-content")
chrome_options.add_argument("--disable-popup-content-titles")
chrome_options.add_argument("disable-gpu")



driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
print(driver.page_source)
print(driver.title)
driver.implicitly_wait(7)
time.sleep(1)

driver.quit()