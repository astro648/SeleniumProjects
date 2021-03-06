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
        title = driver.title
        print("Title of current website: ",title)
        # Get Current Url
        current_url = driver.current_url
        print("Current url: ",current_url)
        # Browser Refresh
        driver.refresh()
        # Open another Url
        driver.get("https://www.nasa.gov/topics/humans-in-space")
        # Browser Back
        driver.back()
        # Browser Forward
        driver.forward()
        # Get Page Source
        # not yet
        while (True):
            pass
        driver.quit()


chrome = RunChromeTest()
chrome.testMethod()