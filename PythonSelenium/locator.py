import time

from selenium import webdriver
from selenium.webdriver.ie.service import Service
from selenium.webdriver.common.by import By

#if company uses vpn or something use this & its faster
serv_obj = Service("/home/raghu/Downloads/chromedriver-linux64/chromedriver")
driver = webdriver.Chrome(service = serv_obj)


try:
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    driver.find_element(By.NAME, "email").send_keys("Raghuu")
    driver.find_element(By.ID, "exampleInputPassword1").send_keys("Raghuuu")
    driver.find_element(By.ID, "exampleCheck1").click()
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    msg = driver.find_element(By.CLASS_NAME, "alert-success").text
    print(msg)
    # assert(msg , "Success! The Form has been submitted successfully!.")

except Exception as e:
    print(e)

time.sleep(2)
driver.close()