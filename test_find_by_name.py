import unittest
from selenium import webdriver


class IdentifyElementByName(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        self.driver.get("http://demo-m2.bird.eu/")

    def test_identify_element_by_name(self):
        self.find_element = self.driver.find_element_by_name('q')
        self.assertTrue(self.find_element.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == '_main__':
    unittest.main(verbosity=2)