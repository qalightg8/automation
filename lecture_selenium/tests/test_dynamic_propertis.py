import time

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from lecture_selenium.helper.usable_methods import wait_until_element_is_enabled, wait_until_element_is_displayed
from lecture_selenium.pages.page_dynamic_proprties import PageDynamicProperties


class TestDynamicProperties:

    def test_dp_1(self, chrome):
        page = PageDynamicProperties(driver=chrome)
        page.open()
        # _id = page.get_enable_after_button_element('id', )
        pass

    def test_dp_2(self, chrome):
        page = PageDynamicProperties(driver=chrome)
        page.open()
        element = page.get_enable_after_button_element()
        WebDriverWait(chrome, 10).until(ec.element_to_be_clickable(element))
        is_element_enabled = element.is_enabled()
        assert is_element_enabled

    def test_dp_3(self, chrome):
        page = PageDynamicProperties(driver=chrome)
        page.open()
        locator = page.visible_after_button_loc
        element = wait_until_element_is_displayed(chrome, locator, max_wait_time=10)

        assert element.is_enabled()
