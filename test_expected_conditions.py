import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

class TestExpectedConditions(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.get('http://demo-store.seleniumacademy.com/')

    def test_presence_of_element(self):
        try:
            WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.ID, "search")))
        except TimeoutException:
            print("Taking more time to load")

    def test_element_located_selection(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.element_located_to_be_selected((By.LINK_TEXT, "English")))
        except TimeoutException:
            print("Taking more time to load")

    def test_invisibility_of_element(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'button')))
        except:
            print("Taking more time to load")

    def test_visibility_of_elements(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'a')))
        except:
            print("Taking more time to load")

    def test_element_to_be_clickable(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(By.XPATH("//button[@title='Subscribe']")))
        except TimeoutException:
            print("Taking more time to load")

    @classmethod
    def tearDown(self):
        self.driver.quit()
