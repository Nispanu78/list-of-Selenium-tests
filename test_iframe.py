import unittest
from selenium import webdriver

class TestIframe(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)

    def test_iframe(self):
        self.iframe1 = self.driver.switch_to_frame("//iframe[@src='https://www.apress.com']")
        self.iframe2 = self.driver.switch_to_frame("//iframe[@src='https://www.bing.com']")
        self.iframe3 = self.driver.switch_to_frame("//iframe[@src='https://www.wikipedia.org']")

    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

