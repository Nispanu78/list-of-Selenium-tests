import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

class TestTimeoutExceptions(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Safari()
        cls.driver.maximize_window()
        cls.driver.get('https://www.apress.com/')

    def test_timeout_exception(self):
        try:
            WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.ID, "query")))
        except TimeoutException:
            print("Taking more time to load")

    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
