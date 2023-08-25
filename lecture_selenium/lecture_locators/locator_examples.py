from selenium.webdriver.common.by import By

By.ID, 'userName'
By.NAME
By.LINK_TEXT
By.PARTIAL_LINK_TEXT


By.CSS_SELECTOR, '[id="userName"]'
By.XPATH, '//[@id, "userName"]'


full_xpath_of_link_home = '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p[1]/a'
simple_xpath_of_link_home = '//div[@id="linkWrapper"]//a[@id="simpleLink"]'