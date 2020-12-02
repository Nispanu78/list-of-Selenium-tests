import unittest
from selenium import webdriver

class TestIframe(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)

        cls.driver.get('https://www.apress.com')

    def test_insert_value(self):

        self.text_box = self.driver.find_element_by_name('query')
        self.text_box.send_keys("Python Testing with Selenium")
        self.text_box.submit()

    def test_get_value(self):
        self.get_value = self.driver.find_element_by_id('book1').get_property('value')
        print(self.get_value)
        self.get_value2 = self.driver.find_element_by_id('book2').get_property('value')
        print(self.get_value2)

    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()