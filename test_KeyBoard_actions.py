import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class KeyBoardActions(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.Firefox(executable_path=r'Macintosh HD/Users/nisp78/Desktop/test/geckodriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        self.driver.get("https://en.wikipedia.org/wiki/Apress")

    def test_key_board_actions(self):
        ActionChains(driver=self.driver) \
            .key_down(Keys.CONTROL) \
            .send_keys("a") \
            .key_up(Keys.CONTROL) \
            .key_down(Keys.CONTROL) \
            .send_keys("c") \
            .key_up(Keys.CONTROL) \
            .perform()

    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()