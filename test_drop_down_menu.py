import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select

class TestDropDownMenu(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)

        cls.driver.get('http://demo-store.seleniumacademy.com/')

    def test_drop_down_by_visible_text(self):
        self.drop_down = Select(self.driver.find_element_by_id('select-language'))
        self.drop_down.select_by_visible_text("English")

    def test_drop_down_multi_select(self):
        self.multi_select = Select(self.driver.find_element_by_id('select-language'))
        self.multi_select.select_by_visible_text("English")
        self.multi_select.select_by_visible_text("French")


    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()