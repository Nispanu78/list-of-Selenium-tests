import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class TestExplicitWait(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.get('https://www.apress.com/')

    def test_explicit_wait(self):
        timeout =10
        try:
        # Returns ID element, when successful
            new_element = WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located((By.ID, "query")))
        # Type "Python with selenium" in search bar
            new_element.send_keys("Python with selenium")
        # Submitting text in search bar
            new_element.send_keys(Keys.ENTER)
        except TimeoutException:
            print("Failed to locate search bar")
        finally:
            self.driver.quit()
        # Closing browser
        self.driver.quit()

    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()