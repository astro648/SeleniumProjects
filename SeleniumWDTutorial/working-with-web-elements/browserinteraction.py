from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class RunChromeTest():
    def testMethod(self):
        global driver
        serv = Service(
            "C:\\Users\\astro\\OneDrive\\Documents\\GitHub\\SeleniumProjects\\drivers\\ChromeDriver\\chromedriver.exe")
        driver = webdriver.Chrome(service=serv)
        purl = "https://www.nasa.gov/"
        driver.get(purl)
        # Window Maximize
        driver.maximize_window()
        # Open the Url
        driver.get(purl)
        # Get Title
        driver.title()
        # Get Current Url

        # Browser Refresh

        # Open another Url

        # Browser Back

        # Browser Forward

        # Get Page Source

        while (True):
            pass
        driver.quit()


chrome = RunChromeTest()
chrome.testMethod()