import unittest
from selenium import webdriver

class FindByTag(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)

        cls.driver.get("http://demo-m2.bird.eu/")

    def test_find_by_tag(self):
        self.find_by_tag = self.driver.find_elements_by_tag_name("ul")
        self.assertEqual(16, len(self.find_by_tag))

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()