import unittest
from selenium import webdriver

class FindElements(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)

        cls.driver.get("http://demo-m2.bird.eu/")

    def test_find_elements(self):
        find_elements = self.driver.find_elements_by_tag_name('a')
        self.assertEqual(82, len(find_elements))

    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()