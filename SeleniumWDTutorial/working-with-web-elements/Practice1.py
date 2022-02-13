from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class RunChromeTest():
    def testMethod(self):
        global driver
        serv = Service(
            "C:\\Users\\astro\\OneDrive\\Documents\\GitHub\\SeleniumProjects\\drivers\\ChromeDriver\\chromedriver.exe")
        driver = webdriver.Chrome(service=serv)
        driver.maximize_window()
        driver.get("https://www.expedia.com/")
        while (True):
            pass
        driver.quit()


chrome = RunChromeTest()
chrome.testMethod()