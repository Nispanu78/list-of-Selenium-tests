import unittest
from selenium import webdriver

class TestAssertEqual(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)

        cls.driver.get('https://www.apress.com')

    def test_assert_equal(self):
        self.title1 = self.driver.title
        self.title2 = "Lamba Home"
        self.assertEqual(self.title1, self.title2, "Title page do not match")

    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()