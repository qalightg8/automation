import pytest
import logging
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.fixture()
def chrome():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def digit():
    yield 5


def test_1(digit):
    assert digit == 5


def test_2(chrome):
    chrome.get('https://demoqa.com/text-box')
    full_name_field = chrome.find_element(By.ID, 'userName')
    full_name_field.send_keys('Vasya')
    full_name_field.send_keys('Pupkin')

    # clear field manually
    # full_name_field.send_keys(Keys.CONTROL + 'A')
    # full_name_field.send_keys(Keys.DELETE)

    # clear field by selenium
    full_name_field.clear()

    full_name_field.send_keys('Petya')
    email_field = chrome.find_element(By.CSS_SELECTOR, '[placeholder="name@example.com"]')
    email_field.send_keys('pupkin@mail.com')
    curr_addr_text_area = chrome.find_element(By.XPATH, '//textarea[@id="currentAddress"]')
    curr_addr_text_area.send_keys('My curr addr in Ukraine')
    perm_addr_text_area = chrome.find_element(By.XPATH, '//textarea[contains(@id, "permanentA")]')
    perm_addr_text_area.send_keys('My perm addr also in Ukraine')
    # submit_button = chrome.find_element(By.XPATH, '//button[.="Submit"]')
    submit_button = chrome.find_element(By.XPATH, '//button[contains(text(), "Sub")]')
    submit_button.click()

    result_name = chrome.find_element().text
    result_name = chrome.find_element(By.).get_attribute('value')

    pass

def test_2():
    logging.info() # name
    logging.info()  # email
    logging.info()  # curr addr
    logging.info()  # perm addr