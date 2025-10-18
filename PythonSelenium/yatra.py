from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.yatra.com/")
driver.maximize_window()
driver.implicitly_wait(5)

xd = driver.find_element(By.XPATH, "//h5[normalize-space()='Special Offers']").text
print(xd)
assert xd == "Special Offers", "Wrong result"
driver.quit()