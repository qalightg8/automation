from selenium.webdriver.common.by import By


def test_scroll_to_book(chrome):
    url = 'https://demoqa.com/books'
    chrome.get(url)
    element = chrome.find_element(By.XPATH, '//a[text()="Understanding ECMAScript 6"]')
    chrome.execute_script("arguments[0].scrollIntoView();", element)  # via JS
    _ = element.location_once_scrolled_into_view  # via find element location (selenium)
    element.click()
