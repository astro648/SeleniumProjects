from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


class RunChromeTest():
    def testMethod(self):
        global driver
        serv = Service(
            "C:\\Users\\astro\\OneDrive\\Documents\\GitHub\\SeleniumProjects\\drivers\\ChromeDriver\\chromedriver.exe")
        driver = webdriver.Chrome(service=serv)
        driver.maximize_window()
        driver.get("http://simplecampus.site/")
        time.sleep(3)
        email_field = driver.find_element(By.ID, "email")
        password_field = driver.find_element(By.ID, "name")
        login_btn = driver.find_element(By.ID, "loginbtn")
        time.sleep(3)
        email_field.send_keys("admin")
        password_field.send_keys("admin")  # these two send the word "admin" to the email and password field
        time.sleep(3)
        email_field.clear() # clears field
        email_field.send_keys("admin")
        time.sleep(3)
        login_btn.click()

        while (True):
            pass
        driver.quit()


chrome = RunChromeTest()
chrome.testMethod()
