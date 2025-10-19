import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class RhSDemo():

    def test1_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.maximize_window()
        print(driver.current_url)
        driver.implicitly_wait(10)

        # Rahul shetty logo verify
        rico = driver.find_element(By.TAG_NAME, "img").is_displayed()
        print(rico)
        assert rico == True, "Wrong result"

        # PRactice Website Text
        prac_page = driver.find_element(By.CSS_SELECTOR, "body h1").text
        print(prac_page)
        assert prac_page == "Practice Page", "Wrong result"

        # Radio Button
        radio_1 = driver.find_element(By.XPATH, "//legend[normalize-space()='Radio Button Example']").text
        print(radio_1)
        assert radio_1 == "Radio Button Example", "Wrong result"
        time.sleep(2)

        if radio_1 == "Radio Button Example":
            click = driver.find_element(By.CSS_SELECTOR, "input[value='radio1']")
            click.click()
            time.sleep(2)
            click2 = driver.find_element(By.CSS_SELECTOR, "input[value='radio3']")
            click2.click()
            time.sleep(1)
            if click.is_selected() and click2.is_selected():
                print("Both are not Selected")
            else:
                print("Both are Selected")

        # country list based on the suggested text entered
        country_text = driver.find_element(By.CSS_SELECTOR, "div[id='select-class-example'] fieldset legend").text
        print(country_text)
        assert country_text == "Suggession Class Example", "Wrong result"

        country_sugg = driver.find_element(By.XPATH, "//input[@id='autocomplete']")
        country_sugg.click()
        time.sleep(1)
        country_sugg.send_keys("Ind")
        time.sleep(1)
        suggest = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] div")
        print(len(suggest))
        for suggests in suggest:
            if suggests.text == "India":
                suggests.click()
                time.sleep(1)
                print(suggests.text)

        # DropDown expample

        dp_1 = driver.find_element(By.XPATH, "//legend[normalize-space()='Dropdown Example']")
        print(dp_1.text)
        print(dp_1.text)
        assert dp_1.text == "Dropdown Example", "Wrong result"

        dp_select = Select(driver.find_element(By.XPATH, "//select[@id='dropdown-class-example']"))
        dp_select.click()
        dp_select.select_by_value("Option2")
        time.sleep(1)
        dp_select.select_by_index(1)
        time.sleep(1)

        # Multiple option select

        Mul_1 = driver.find_element(By.CSS_SELECTOR, "div[id='checkbox-example'] fieldset legend")
        print(Mul_1.text)
        print(Mul_1.text)
        assert Mul_1.text == "Checkbox Example", "Wrong result"

        op1 = driver.find_element(By.CSS_SELECTOR, "#checkBoxOption1")
        op1.click()
        time.sleep(1)
        if op1.is_selected():
            print("Selected")
        else:
            print("Not Selected")

        op2 = driver.find_element(By.CSS_SELECTOR, "#checkBoxOption2")
        op2.click()
        time.sleep(1)
        if op2.is_selected():
            print("Selected")
        else:
            print("Not Selected")

        # Switch Window Example

        sw_1 = driver.find_element(By.XPATH, "//legend[normalize-space()='Switch Window Example']")
        print(sw_1.text)
        assert sw_1.text == "Switch Window Example", "Wrong result"

        # sw_click = driver.find_element(By.CSS_SELECTOR, "#openwindow")
        # sw_click.click()
        # time.sleep(1)

        alert_1 = driver.find_element(By.CSS_SELECTOR, "fieldset[class='pull-right'] legend")
        print(alert_1.text)
        assert alert_1.text == "Switch To Alert Example", "Wrong result"

        alert_fn = driver.find_element(By.CSS_SELECTOR, "#name")
        alert_fn.send_keys("Raghuu")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
        time.sleep(1)
        js = driver.switch_to.alert
        js.accept()










        driver.quit()

dem_obj = RhSDemo()
dem_obj.test1_demo()


















