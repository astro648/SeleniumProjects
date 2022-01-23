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

        elementsById = driver.find_element(By.ID,"name")

        if elementsById is not None:
            print("We found an element by Id")


        while (True):
            pass

        driver.quit()

ff = ListOfElements()
ff.test()