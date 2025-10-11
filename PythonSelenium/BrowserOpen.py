import time

from selenium import webdriver
from selenium.webdriver.ie.service import Service

#if company uses vpn or something use this & its faster
serv_obj = Service("/home/raghu/Downloads/chromedriver-linux64/chromedriver")
driver = webdriver.Chrome(service = serv_obj)
driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

# driver = webdriver.Chrome()
# driver.get("https://google.com")












time.sleep(2)
driver.close()