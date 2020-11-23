import unittest
from selenium import webdriver

class FindByLink(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)

        cls.driver.get("http://demo-m2.bird.eu/")

    def test_find_by_link(self):
        find_link = self.driver.find_element_by_link_text('Home')
        self.assertTrue(find_link.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()