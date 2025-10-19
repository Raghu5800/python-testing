import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://semantic-ui.com/modules/dropdown.html")
driver.maximize_window()

drop = driver.find_element(By.XPATH, "//div[@class='dropdown example']//div[@class='default text'][normalize-space()='Gender']")
drop.click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "div[class='menu transition visible'] div:nth-child(1)").click()
time.sleep(2)
drop.click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "div[class='menu transition visible'] div:nth-child(2)").click()
time.sleep(2)