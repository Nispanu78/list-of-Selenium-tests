import unittest
from selenium import webdriver

class IdentifyElement(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        self.driver.get("http://demo-m2.bird.eu/")

    def test_identify_element(self):
        self.find_element = self.driver.find_element_by_id('switcher-language')
        self.assertTrue(self.find_element.is_displayed())

    def TearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)

# import unittest
# from selenium import webdriver
#
#
# class SearchTests(unittest.TestCase):
#     def setUp(self):
#         # create a new Firefox session
#         self.driver = webdriver.Firefox()
#         self.driver.implicitly_wait(30)
#         self.driver.maximize_window()
#
#         # navigate to the application home page
#         self.driver.get('http://demo-store.seleniumacademy.com/')
#
#     def test_search_by_category(self):
#         # get the search textbox
#         self.search_field = self.driver.find_element_by_name('q')
#         self.search_field.clear()
#
#     def tearDown(self):
#         # close the browser window
#         self.driver.quit()
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)