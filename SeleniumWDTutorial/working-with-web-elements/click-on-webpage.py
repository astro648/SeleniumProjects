from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class RunChromeTest():
    def testMethod(self):
        global driver
        serv = Service(
            "C:\\Users\\astro\\OneDrive\\Documents\\GitHub\\SeleniumProjects\\drivers\\ChromeDriver\\chromedriver.exe")
        driver = webdriver.Chrome(service=serv)
        driver.maximize_window()
        driver.get("http://simplecampus.site/")
        driver.find_element(By.ID, "email")
        driver.find_element(By.ID, "password")
        while (True):
            pass
        driver.quit()


chrome = RunChromeTest()
chrome.testMethod()
