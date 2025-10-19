import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.yatra.com/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "span[class='style_cross__q1ZoV'] img[alt='cross']").click()
time.sleep(2)

parent = driver.current_window_handle
print(parent)


driver.find_element(By.XPATH, "//div[@title='Fly The Malaysian Way']//div[@class='MuiBox-root css-1dhsmro']").click()
time.sleep(2)
all_handles = driver.window_handles
print(all_handles)
for handle in all_handles:
    if handle != parent:
        driver.switch_to.window(handle)
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[normalize-space()='Hotels']").click()
        time.sleep(2)
        driver.close()
        time.sleep(2)
        break

driver.switch_to.window(parent)
time.sleep(2)

driver.find_element(By.XPATH, "//div[@title='Fly The Malaysian Way']//div[@class='MuiBox-root css-1dhsmro']").click()
time.sleep(2)

driver.quit()


