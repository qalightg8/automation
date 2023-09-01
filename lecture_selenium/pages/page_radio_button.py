from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PageRadioButton:
    __URL = 'https://demoqa.com/radio-button'

    def __init__(self, driver: WebDriver):
        self.__driver = driver
        self.__yes_radio_button_xpath = '//label[@for="yesRadio"]//ancestor::div[contains(@class, "radio")]'
        self.__impressive_radio_button_xpath = '//label[@for="impressiveRadio"]//ancestor::div[contains(@class, "radio")]'

    def open(self):
        self.__driver.get(self.__URL)

    def __select_button_by_locator(self, xpath: By.XPATH):
        self.__driver.find_element(By.XPATH, xpath).click()

    def select_yes_button(self):
        locator = self.__yes_radio_button_xpath + '/label'
        self.__select_button_by_locator(locator)

    def select_impressive_button(self):
        locator = self.__impressive_radio_button_xpath + '/label'
        self.__select_button_by_locator(locator)

    def is_yes_button_selected(self) -> bool:
        locator = self.__yes_radio_button_xpath + '/input'
        return self.__driver.find_element(By.XPATH, locator).is_selected()

    def is_impressive_button_selected(self) -> bool:
        locator = self.__impressive_radio_button_xpath + '/input'
        return self.__driver.find_element(By.XPATH, locator).is_selected()
