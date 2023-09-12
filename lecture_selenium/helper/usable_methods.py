import time
from datetime import datetime

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def get_element_text_by_xpath(driver: WebDriver, locator: By.XPATH) -> str:
    return driver.find_element(*locator).text


def wait_until_element_is_enabled(element: WebElement, max_wait_time=10, polling_time=0.1) -> bool:
    end_time = time.monotonic() + max_wait_time
    while time.monotonic() < end_time:
        if element.is_enabled():
            break
        else:
            time.sleep(polling_time)
            continue
    return element.is_enabled()


def wait_until_element_is_displayed(driver: WebDriver, locator: tuple, max_wait_time=10, polling_time=0.1) -> WebElement | None:
    end_time = time.monotonic() + max_wait_time
    element = None
    while time.monotonic() < end_time:
        try:
            element = driver.find_element(*locator)
            break
        except NoSuchElementException:
            time.sleep(polling_time)
            continue
    return element
