import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ImplicitWait(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        self.driver.get("http://apress.com")
        print("It's an implicit wait")

    def test_implicit_wait(self):
        self.find_element = self.driver.find_element_by_id('query')
        self.find_element.send_keys("Python with selenium")
        self.find_element.submit()

    def tearDown(self):
        self.driver.quit()

if __name__ == '_main__':
    unittest.main(verbosity=2)