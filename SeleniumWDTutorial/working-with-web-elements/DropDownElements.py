from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class DropDownElements():
    def testMethod(self):
        global driver
        serv = Service("C:\\Users\\alexemtech\\workspace_python\\drivers\\chromedriver.exe")
        driver = webdriver.Chrome(service=serv)
        driver.maximize_window()
        driver.get("http://www.alexemtech.com/practice")
        driver.implicitly_wait(10)

        element = driver.find_element(By.ID, "carselect")
        sel = Select(element)

        # Select by Value
        sel.select_by_value("benz")
        print("Select Benz by Value")
        time.sleep(2)

        # Select By Index
        sel.select_by_index("2")
        print("Select Honda by index")
        time.sleep(2)

        # Select by Visible Text
        sel.select_by_visible_text("BMW")
        print("Select BMW by Visible Text")
        time.sleep(2)

        # 2nd Way to Select by index
        sel.select_by_index(2)
        print("Select Honda by index")

chr = DropDownElements()
chr.testMethod()