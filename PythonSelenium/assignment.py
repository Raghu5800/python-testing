import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()

handle = driver.window_handles
driver.switch_to.window(handle[1])

email = driver.find_element(By.CSS_SELECTOR, ".im-para.red").text
print(email)
words = email.split()

for word in words:
    if '@' in word:
        email = word.strip('.,')
        print(email)

driver.switch_to.window(handle[0])

driver.find_element(By.CSS_SELECTOR, "#username").send_keys(email)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("Dummy")
driver.find_element(By.CSS_SELECTOR, "#terms").click()
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
time.sleep(4)
error = driver.find_element(By.XPATH, "//div[@class='alert alert-danger col-md-12']/strong['Incorrect username/password']")
time.sleep(2)
print(error.text)
