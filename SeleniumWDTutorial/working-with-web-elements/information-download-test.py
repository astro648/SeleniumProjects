from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class RunChromeTest():
    def testMethod(self):
        global driver
        serv = Service(
            "C:\\Users\\astro\\OneDrive\\Documents\\GitHub\\SeleniumProjects\\drivers\\ChromeDriver\\chromedriver.exe")
        driver = webdriver.Chrome(service=serv)
        driver.maximize_window()
        driver.get("https://www.bisegrw.edu.pk/")
        driver.implicitly_wait(10000)
        close_btn = driver.find_element(By.CLASS_NAME, "fancybox-close")
        close_btn.click()
        time.sleep(2)
        element = driver.find_element(By.CLASS_NAME, "clsname")
        sel = Select(element)
        sel.select_by_visible_text("12th Annual")
        print("Select 12th Annual by Visible Text")
        time.sleep(2)
        rollno_enter = driver.find_element(By.CLASS_NAME, "clsrno")
        rollno_enter.send_keys("155797")
        print("typed in rollno")
        time.sleep(2)
        search_btn = driver.find_element(By.CLASS_NAME,"search")
        search_btn.click()
        print("search btn clicked")
        time.sleep(2)

        while (True):
            pass
        driver.quit()


chrome = RunChromeTest()
chrome.testMethod()