import unittest
from selenium import webdriver
import page

class ApressSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.apress.com")

    def test_apress_search(self):
        home_page = page.HomePage(self.driver)
        home_page.search_text ="Python Selenium"
        home_page.click_submit_button()
        search_results_page = page.ResultPage(self.driver)
        
        assert search_results_page.check_search_results(), "No results found."
    def tearDown(self):
        self.driver.close()
if __name__ =="__main__":
    unittest.main()