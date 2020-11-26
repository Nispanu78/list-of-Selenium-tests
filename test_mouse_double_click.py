import unittest
from selenium import webdriver

class MouseDoubleClick(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        self.driver.get("http://www.apress.com")

    def test_mouse_click_and_hold(self):
        button = self.driver.find_element_by_link_text("Apress Access")
        webdriver.ActionChains(driver=self.driver).double_click(button).perform()

    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()