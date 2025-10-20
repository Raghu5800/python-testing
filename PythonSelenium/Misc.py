import time

from selenium import webdriver

# Chrome options to run as headless & avoid certification / security error
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--avoid--certificate-errors")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);") # widely used for locator find & running it use it & check it in console
time.sleep(1)
driver.get_screenshot_as_file("screen.png")




