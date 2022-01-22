from selenium import webdriver
from selenium.webdriver.edge.service import Service


class RunMSEdgeTest():
    def testMethod(self):
        global driver
        serv = Service(
            "C:\\Users\\astro\\OneDrive\\Documents\\GitHub\\SeleniumProjects\\drivers\\EdgeDriver\\msedgedriver.exe")
        driver = webdriver.Edge(service=serv)
        driver.maximize_window()
        driver.get("https://www.nasa.gov/")
        while (True):
            pass
        driver.quit()


edge = RunMSEdgeTest()
edge.testMethod()