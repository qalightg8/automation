from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PageTextBox:
    URL = 'https://demoqa.com/text-box'

    def __init__(self, driver: WebDriver):
        self.__driver = driver
        self.__full_name_field_loc = (By.XPATH, '//input[@id="userName"]')
        self.__email_field_loc = (By.XPATH, '//input[@id="userEmail"]')
        self.__curr_addr_text_area_loc = (By.XPATH, '//textarea[@placeholder="Current Address"]')
        self.__perm_addr_text_area_loc = (By.XPATH, '//textarea[@id="permanentAddress"]')
        self.__submit_button_loc = (By.XPATH, '//button[.="Submit"]')
        self.__button_loc = (By.XPATH,
                             '//button[.="{}"]')  # any button with name taken as argument from corresponded method (instead of curves brackets)#

    def open(self):
        self.__driver.get(self.URL)

    def set_full_name(self, fullname: str) -> None:
        element = self.__driver.find_element(*self.__full_name_field_loc)
        element.clear()
        element.send_keys(fullname)

    def set_email(self, email: str) -> None:
        element = self.__driver.find_element(*self.__email_field_loc)
        element.clear()
        element.send_keys(email)

    def set_current_address(self, address: str) -> None:
        element = self.__driver.find_element(*self.__curr_addr_text_area_loc)
        element.clear()
        element.send_keys(address)

    def set_permanent_address(self, perm_address: str) -> None:
        element = self.__driver.find_element(*self.__perm_addr_text_area_loc)
        element.clear()
        element.send_keys(perm_address)

    def submit(self) -> None:
        element = self.__driver.find_element(*self.__submit_button_loc)
        element.click()

    def click_button_by_name(self, button_name) -> None:
        by = self.__button_loc[0]
        loc = self.__button_loc[1].format(button_name)
        element = self.__driver.find_element(by, loc)
        # index [1] used, because locator 'self.__button_loc' is a tuple, and we need to work only with text part of locator#
        element.click()
