import unittest
from selenium import webdriver

class WorkingWithElements(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        # cls.driver.maximize_window()
        # to open the window browser with a specific size.
        # cls.driver.set_window_size(500, 400)
        # to open the browser window by using coordinates
        # cls.driver.set_window_rect(x=30, y=30, width=450, height=500)

        cls.driver.implicitly_wait(80)

        cls.driver.get("http://demo-m2.bird.eu/")

        # to identify the position of the browser according to x,y axes)
        window_pos = cls.driver.get_window_position()
        print(window_pos)

        window_size = cls.driver.get_window_size()
        print(window_size)

    def test_working_with_elements(self):
        self.driver.WorkingWithElements = self.driver.find_element_by_name('q')
        self.driver.WorkingWithElements.clear()
        # enter a text value in a text box
        self.driver.WorkingWithElements.send_keys("tops")
        # submits the value
        # self.driver.WorkingWithElements.submit()
        # click on the search button once the value has been submitted
        self.driver.WorkingWithElements.click()

    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

