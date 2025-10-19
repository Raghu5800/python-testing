import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.implicitly_wait(10)

# parent window
driver.find_element(By.LINK_TEXT, "Click Here").click()
time.sleep(2)
winOpen = driver.window_handles

# navigates to child window
driver.switch_to.window(winOpen[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()
time.sleep(2)


driver.switch_to.window(winOpen[0])
print(driver.find_element(By.TAG_NAME, "h3").text)

driver.quit()



