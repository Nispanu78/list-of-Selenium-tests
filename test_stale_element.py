import unittest
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://www.apress.com/')

driver.find_element_by_id('query').send_keys("selenium")
while True:
    try:
        s=driver.find_element_by_class_name('search__submit')
        s.submit()
        time.sleep(2)
        s.submit()
    except StaleElementReferenceException:
        print('Stale Exception is Skipped.')
    break

driver.quit()

if __name__ == "__main__":
    unittest.main()