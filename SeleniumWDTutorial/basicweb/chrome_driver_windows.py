from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class RunChromeTest():
    def testMethod(self):
        serv = Service("C:\\Users\\astro\\OneDrive\\Documents\\GitHub\\SeleniumProjects\\drivers\\Mozilla - Gecko "
                       "Driver\\geckodriver.exe")
        driver = webdriver.Firefox(service=serv)
        driver.maximize_window()
        driver.get("https://www.nasa.gov/")


chrome = RunChromeTest()
chrome.testMethod()
