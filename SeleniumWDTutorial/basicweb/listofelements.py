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

        elementsByClassName = driver.find_elements(By.CLASS_NAME,"inputs")
        length = len(elementsByClassName)

        if elementsByClassName is not None:
            print("We found",length,"elements by class name")

        elementsByTagName = driver.find_elements(By.TAG_NAME, "div")
        length1 = len(elementsByTagName)

        if elementsByTagName is not None:
            print("We found", length1, "elements by tag name")


        while (True):
            pass

        driver.quit()

ff = ListOfElements()
ff.test()