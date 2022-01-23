from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
class ListOfElements():

    def test(self):
        global driver
        serv = Service(
            "C:\\Users\\astro\\OneDrive\\Documents\\GitHub\\SeleniumProjects\\drivers\\ChromeDriver\\chromedriver.exe")
        driver = webdriver.Chrome(service=serv)
        driver.maximize_window()
        driver.get("https://www.alexemtech.com/practice/")

        elementById = driver.find_element(By.ID,"name")

        if elementById is not None:
            print("We found an element by Id")

        elementByXpath = driver.find_element(By.XPATH,"//input[@id='displayed-text']")

        if elementByXpath is not None:
            print("We found an element by XPATH")

        elementByLinkText = driver.find_element(By.LINK_TEXT,"Open Tab")

        if elementByLinkText is not None:
            print("We found an element by Link Text")


        while (True):
            pass

        driver.quit()

ff = ListOfElements()
ff.test()