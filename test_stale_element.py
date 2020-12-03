import unittest
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
import time

class TestStaleElement(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Safari()
        cls.driver.maximize_window()
        cls.driver.get('https://www.apress.com/')

    def test_stale_element(self):
        self.driver.find_element_by_name('query').send_keys('selenium')
        while True:
            try:
                s=self.driver.find_element_by_class_name('search__submit')
                s.submit()
                time.sleep(2)
                s.submit()
            except StaleElementReferenceException:
                print('Stale Exception is Skipped.')
            break

    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()