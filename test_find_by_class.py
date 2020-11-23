import unittest
from selenium import webdriver


class FindByClassAttribute(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)

        cls.driver.get("http://demo-m2.bird.eu/")

    def test_find_by_class_attribute_2(self):
        class_attribue2 = self.driver.find_element_by_class_name('page-wrapper')
        self.assertTrue(class_attribue2.is_displayed())

    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
