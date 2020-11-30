from selenium import webdriver
driver=webdriver.Firefox()
# Navigate to page stored as local file
driver.get("drag_and_drop.html")
# Locate 'drag' element as source
element1 =driver.find_element_by_id("drag")
# Locate 'drop' element as target
element2=driver.find_element_by_id("drop")
# Perform drag and drop action from
webdriver.ActionChains(driver).drag_and_drop(element1,element2).perform()
