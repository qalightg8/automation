from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PageCheckbox:
    __URL = 'https://demoqa.com/checkbox'

    def __init__(self, driver: WebDriver):
        self.__driver = driver
        self.__expand_collapse_button = '//span[text()="{}"]//ancestor::span/button/*[contains(@class, "icon-expand")]'
        self.__check_uncheck_label = '//label[@for="tree-node-{}"]'

    def open(self):
        self.__driver.get(self.__URL)

    def expand_node_by_name(self, name):
        trigger = 'close'
        self.__expand_or_collapse_node(name=name, trigger=trigger)

    def collapse_node_by_name(self, name):
        trigger = 'open'
        self.__expand_or_collapse_node(name=name, trigger=trigger)

    def __expand_or_collapse_node(self, name, trigger):
        xpath = self.__expand_collapse_button.format(name)
        element = self.__driver.find_element(By.XPATH, xpath)
        if trigger in element.get_attribute('class'):
            element.click()

    def expand_nodes_from_list(self, nodes: list):
        for node in nodes:
            self.expand_node_by_name(node)

    def check_folder(self, name: str):
        check_uncheck_input = f'{self.__check_uncheck_label.format(name.lower())}/input'
        check_uncheck_label = f'{check_uncheck_input}/..'
        _input = self.__driver.find_element(By.XPATH, check_uncheck_input)
        _label = self.__driver.find_element(By.XPATH, check_uncheck_label)
        if not _input.is_selected():
            _label.click()

    def uncheck_folder(self, name: str):
        check_uncheck_input = f'{self.__check_uncheck_label.format(name.lower())}/input'
        check_uncheck_label = f'{check_uncheck_input}/..'
        _input = self.__driver.find_element(By.XPATH, check_uncheck_input)
        _label = self.__driver.find_element(By.XPATH, check_uncheck_label)
        if _input.is_selected():
            _label.click()

    # TODO: make it DRY
