import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class TestElementNotFound(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.get('https://www.apress.com/')

    def test_element_not_found(self):
        try:
            web1 =self.driver.find_element_by_id("Fernando")
            web1.click()
        except NoSuchElementException as exception:
            print ("Web Element is not Available in the given Web Page.")

    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()