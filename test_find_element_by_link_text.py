import unittest
from selenium import webdriver

class FindByLinktext(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)

        cls.driver.get("http://demo-m2.bird.eu/")

    def test_find_by_link_text(self):
        self.find_by_link = self.driver.find_element_by_xpath("""//strong[@ data-bind="visible: closeSidebar(), i18n: 'You have no items in your shopping cart.'"]""").text

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
