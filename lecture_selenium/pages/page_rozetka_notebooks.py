from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PageRozetkaNotebooks:
    __URL = 'https://rozetka.com.ua/ua/notebooks/c80004/'

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.__goods_card_loc = (By.XPATH, '//li[contains(@class, "catalog-grid__cell")]')
        self.__paginator_loc = (By.XPATH, '//div[starts-with(@class, "pagination")]')

    def open(self):
        self.driver.get(self.__URL)

    def get_goods_count(self) -> int:
        elements = self.driver.find_elements(*self.__goods_card_loc)
        return len(elements)

    def get_goods_names(self) -> list:
        goods = self.driver.find_elements(*self.__goods_card_loc)
        return [product.text for product in goods]

    def is_scroll_to_paginator_works(self) -> bool:
        element = self.driver.find_element(*self.__paginator_loc)
        _ = element.location_once_scrolled_into_view
        try:
            WebDriverWait(self.driver, 1).until(expected_conditions.element_to_be_clickable(element))
            return True
        except TimeoutError:
            return False

    def scroll_to_last_goods(self):
        pass
