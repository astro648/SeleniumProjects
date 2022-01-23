from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class RunChromeTest():
    def testMethod(self):
        global driver
        serv = Service(
            "C:\\Users\\astro\\OneDrive\\Documents\\GitHub\\SeleniumProjects\\drivers\\ChromeDriver\\chromedriver.exe")
        driver = webdriver.Chrome(service=serv)
        driver.maximize_window()
        driver.get("https://www.alexemtech.com/practice/")
        elementbyid = driver.find_element_by_id("name")
        if elementbyid is not None:
            print("Found an element by ID")

        elementbyname = driver.find_element_by_name("courses")
        if elementbyname is not None:
            print("Found an element by name")

        elementbylinktext = driver.find_element_by_link_text("Open Tab")
        if elementbylinktext is not None:
            print("Found an element by link text")


        while (True):
            pass

        driver.quit()


chrome = RunChromeTest()
chrome.testMethod()