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
        driver.get("https://www.expedia.com/?pwaLob=wizard-flight-pwa")
        driver.implicitly_wait(10)

        textBoxElement = driver.find_element(By.NAME, "toDate")
        textBoxState = textBoxElement.is_displayed()  # True if visible, false if hidden
        print("Text is visible? " + str(textBoxState))
        time.sleep(2)

        driver.get("https://www.expedia.com/?flightType=oneway")
        driver.implicitly_wait(10)
        textBoxElement = driver.find_element(By.NAME, "toDate")
        textBoxState = textBoxElement.is_displayed()  # True if visible, false if hidden
        print("Text is visible? " + str(textBoxState))
        time.sleep(2)


chr = RunChromeTest()
chr.testMethod()
