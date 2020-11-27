import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class MoveToAnElement(unittest.TestCase):
    @classmethod
    def setUp(self):
        # self.driver = webdriver.Firefox(executable_path=r'Macintosh HD/Users/nisp78/Desktop/test/geckodriver.exe')
        self.driver = webdriver.Safari()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        self.driver.get("http://www.apress.com")

    def test_mouse_click_and_hold(self):
        self.main_menu = self.driver.find_element_by_link_text("CATEGORIES")
        ActionChains(driver=self.driver).move_to_element(self.main_menu).perform()

        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.LINK_TEXT, "Python")))

        sub_menu = self.driver.find_element_by_link_text("Python")
        sub_menu.click()

    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

