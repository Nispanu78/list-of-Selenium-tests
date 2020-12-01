import unittest
from selenium import webdriver

class TestRadioButton(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)

        cls.driver.get('https://www.apress.com/')

    def test_find_button(self):
        self.find_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        self.find_button.is_displayed()
        self.find_button.click()

    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()