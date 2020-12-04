from selenium.webdriver.support.ui import WebDriverWait

class BasePageElement(object):
#Used in every page
    def _set_(self, obj, value):
#Contains specified text
        driver = obj.driver
        WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_name(self.locator))
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)
    def __get__(self, obj, owner):
# Gets the text of the specified object
        driver = obj.driver
        WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")