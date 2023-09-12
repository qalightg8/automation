import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def chrome():
    options = Options()
    # options.add_argument('--start-maximized')
    # options.add_argument('--force-device-scale-factor=0.75')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
