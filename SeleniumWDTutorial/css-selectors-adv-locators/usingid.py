from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
class usingID():
    def test(self):
        global driver
        serv = Service(
            "C:\\Users\\astro\\OneDrive\\Documents\\GitHub\\SeleniumProjects\\drivers\\ChromeDriver\\chromedriver.exe")
        driver = webdriver.Chrome(service=serv)
        driver.maximize_window()
        driver.get("https://www.alexemtech.com/practice/")

        elementsByID = driver.find_elements(By.ID, "radio-btn-example")
        length = len(elementsByID)

        if elementsByID is not None:
            print("We found",length,"elements by ID")



        while (True):
            pass

        driver.quit()