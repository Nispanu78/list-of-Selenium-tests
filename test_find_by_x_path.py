import unittest
from selenium import webdriver

class FindByXPath(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)

        cls.driver.get("http://demo-m2.bird.eu/")

    def test_by_x_path(self):
        self.find_by_x_path = self.driver.find_element_by_xpath("//a[@id='iduQmg2fVY']")
        self.find_by_x_path.click()

    def test_by_x_path_starts_with(self):
        self.find_by_starts_with = self.driver.find_element_by_xpath("//div[starts-with(@ class, 'minicart')]")
        self.find_by_starts_with.click()

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()

