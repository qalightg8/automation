from selenium.webdriver.remote.webdriver import WebDriver


class Button:
    def __init__(self, driver: WebDriver, locator):
        self.__driver = driver
        self.__locator = locator

    def click(self):
        self.__driver.find_element(self.__locator).click()


button2 = Button(driver=WebDriver, locator='//sdfsgsg')
button2.click()
