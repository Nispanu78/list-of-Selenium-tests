import unittest
from selenium import webdriver

class FindByCSSSelector(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)

        cls.driver.get("http://demo-m2.bird.eu/")

    def test_find_minicart_by_css_selector(self):
        self.find_minicart_by_absolute_path = self.driver.find_element_by_css_selector("html body div header div div a")
        self.assertTrue(self.find_minicart_by_absolute_path.is_displayed())

    def test_find_minicart_by_css_selector_and_class(self):
        self.find_minicart_by_css_and_class = self.driver.find_element_by_css_selector("span.text").text
        self.assertEqual("My Cart", self.find_minicart_by_css_and_class)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()