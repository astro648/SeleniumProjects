# imports class from webdriver
from selenium import webdriver
# import service for firefox (S in Service is capital)
from selenium.webdriver.firefox.service import Service


class RunFFTest():
    def testMethod(self):
        # Use dir of gecko driver
        serv = Service("C:\\Users\\astro\\OneDrive\\Documents\\GitHub\\SeleniumProjects\\drivers\\Mozilla - Gecko "
                       "Driver\\geckodriver.exe")
        # from selenium firefox driver import service
        driver = webdriver.Firefox(service=serv)
        # maximizes window
        driver.maximize_window()
        # get site that you want to use
        driver.get("https://www.nasa.gov/")


ff = RunFFTest()
ff.testMethod()

# Above code lets us open the site in Firefox and it is remote-controlled by the webdriver in dev mode
