from page_objects.elements import BasePageElement
from page_objects.locators import HomePageLocators

class SearchText(BasePageElement):
#The locator for search box where search string is entered
    locator ='query'

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class HomePage(BasePage):
#Actions items for Home Page
#Variable containing retrieved text
    search_text = SearchText()

    def click_submit_button(self):
#Search is initialized
        element=self.driver.find_element(*HomePageLocators.SUBMIT_BUTTON)
        element.click()

class ResultPage(BasePage):
#Actions items for result page
    def check_search_results(self):
# Checks the result for specified text if found or not
        return "No results found." not in self.driver.page_source