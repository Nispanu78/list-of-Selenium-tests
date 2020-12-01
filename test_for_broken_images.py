import unittest
import requests
from selenium import webdriver

class TestForBrokenImages(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)

        cls.driver.get("http://www.apress.com")

    def test_broken_images(self):
        images = self.driver.find_elements_by_tag_name('img')
        for image in images:
            if (requests.head(image.get_attribute('src')).status_code == 200):
                print("Valid image link")
            else:
                print("Broken image link")

    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()