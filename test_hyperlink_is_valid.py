import unittest
import requests
from selenium import webdriver

class TestHyperlinkIsValid(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)

        cls.driver.get("http://www.apress.com")

    def test_hyperlink_validity(self):
        find_hyperlink = self.driver.find_elements_by_tag_name('a')
        for hyperlink in find_hyperlink:
            if (requests.head(hyperlink.get_attribute('href')).status_code == 200):
                print("Link is valid.")
            else:
                print("Link is broken")

    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()