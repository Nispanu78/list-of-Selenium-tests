import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class MoveToAnElement(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.Firefox(executable_path=r'Macintosh HD/Users/nisp78/Desktop/test/geckodriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        self.driver.get("http://www.apress.com")

    def test_mouse_by_offset(self):
        x = 268
        y = 66
        ActionChains(driver=self.driver).move_by_offset(x, y).perform()
        # # self.element = self.driver.find_element_by_link_text("CATEGORIES")
        # # action = ActionChains(driver=self.driver)
        # # action.move_to_element_with_offset(self.element, 200, 50).click().perform()

    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

