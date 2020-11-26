import unittest
from selenium import webdriver


class TestBrowserNavigationTools(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)

        #Open apress webpage
        cls.driver.get('https://apress.com')
        #Open Google page
        cls.driver.get('https://google.com')
        #Go back to previous 'apress' page
        cls.driver.back()
        print("Moved to first page")
        cls.driver.forward()
        print("Moved to second page")
        #Page refresh command
        cls.driver.refresh()
        print("Page is Refreshed")

    def test_navigation_tools(self):
        pass

    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
























