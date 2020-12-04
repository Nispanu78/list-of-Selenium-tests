import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotSelectableException

class TestFluentWait(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.get('https:/www.apress.com')

    def test_fluent_wait(self):
        self.timeout = 10
        self.wait = WebDriverWait(self.driver, self.timeout, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        self.new_element = self.wait.until(EC.presence_of_element_located((By.ID, "query")))

    @classmethod
    def tearDown(self):
        self.driver.quit()