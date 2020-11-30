import unittest
import requests
from selenium import webdriver

class FindElements(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)

        cls.driver.get("http://www.apress.com")

    def test_find_elements(self):
        find_elements = self.driver.find_elements_by_tag_name('img')
        for element in find_elements:
            if (requests.head(element.get_attribute('src')).status_code == 200):
                print("Element Found.")

    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()