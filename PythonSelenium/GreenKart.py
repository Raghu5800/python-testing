import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(10) # implicit wait command
# explicit wait is for element specific wait

driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search for Vegetables and Fruits']").send_keys("ber")
time.sleep(2)

prod_exist = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
prod_name = driver.find_elements(By.CSS_SELECTOR, "div h4[class='product-name']")
f_list = []
for prod in prod_name:
    f_list.append(prod.text)

print(f_list)



assert prod_exist == f_list, "The product name doesn't match the product name"

result = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(result)
assert count > 0

for i in result:
   # another way of storing & comapring with exisitng list f_list.append(i.find_element(By.CSS_SELECTOR, "div h4[class='product-name']"))
    i.find_element(By.XPATH,".//div/button" ).click()


pop = driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']")
pop.click()
assert pop.is_displayed(), "Error"

driver.find_element(By.XPATH, "//button[normalize-space()='PROCEED TO CHECKOUT']").click()

# func validation
total = driver.find_elements(By.XPATH , "//tr/td[5]/p")
sum = 0
for i in total:
    sum += int(i.text)
print(sum)
TotalAmt = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
print(TotalAmt)
assert sum == TotalAmt, "Error"

driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()

wait = WebDriverWait(driver, 10)
promo_code = wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

disc_amt = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
print(f"Discount Amount:",disc_amt)
assert TotalAmt > disc_amt, "Error"

#promo_success = driver.find_element(By.CSS_SELECTOR, ".promoInfo")
print(promo_code.text)
assert promo_code.is_displayed(), "Error"
assert promo_code.text == "Code applied ..!", "Error"

driver.quit()