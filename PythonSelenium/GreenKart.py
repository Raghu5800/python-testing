import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search for Vegetables and Fruits']").send_keys("ber")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(5)

# add to cart
driver.find_element(By.XPATH, "//div[@class='products']//div[1]//div[3]//button[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='products']//div[1]//div[3]//button[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@class='products']//div[1]//div[3]//button[1]").click()
time.sleep(2)

#open cart
driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//button[normalize-space()='PROCEED TO CHECKOUT']").click()

time.sleep(2)

# payment Board

veg1 = driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/p[1]").text
print(veg1)

veg2 = driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/p[1]").text
print(veg2)

veg3 = driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/p[1]").text
print(veg3)

length = len(veg1)+len(veg2)+len(veg3)
print(length)