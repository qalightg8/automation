from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PagePracticeForm:
    __URL = 'https://demoqa.com/automation-practice-form'

    def __init__(self, driver: WebDriver):
        self.__driver = driver
        self.__state_city_wrapper_loc = '//div[@id="stateCity-wrapper"]'
        self.__state_dropdown_menu_loc = '//div[@id="state"]'
        self.__state_dropdown_element_loc = '//div[text()="{}"]'

    def open(self):
        self.__driver.get(self.__URL)

    def __get_xpath_for_state_dropdown(self) -> str:
        wrapper = self.__state_city_wrapper_loc
        menu = self.__state_dropdown_menu_loc
        xpath = f'{wrapper}{menu}'
        return xpath

    def __expand_states(self):
        dropdown_menu = self.__driver.find_element(By.XPATH, self.__get_xpath_for_state_dropdown())
        # ActionChains(self.__driver).scroll_to_element(dropdown_menu).perform()
        # ActionChains(self.__driver).move_to_element(dropdown_menu).perform()
        # self.__driver.execute_script("arguments[0].scrollIntoView();", dropdown_menu)
        # _ = dropdown_menu.location_once_scrolled_into_view
        dropdown_menu.click()

    def __select_state_by_name(self, name):
        state_xpath = f'{self.__get_xpath_for_state_dropdown()}{self.__state_dropdown_element_loc.format(name)}'
        state_element = self.__driver.find_element(By.XPATH, state_xpath)
        # ActionChains(self.__driver).scroll_to_element(state_element).perform()
        # ActionChains(self.__driver).move_to_element(state_element).perform()
        # self.__driver.execute_script("arguments[0].scrollIntoView();", state_element)
        # _ = state_element.location_once_scrolled_into_view
        state_element.click()

    def select_state(self, name):
        self.__expand_states()
        self.__select_state_by_name(name)
        pass
