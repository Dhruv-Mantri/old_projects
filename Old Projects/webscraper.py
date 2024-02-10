from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
path = "C:\\Users\mandh\Documents\chromedriver.exe"

google = "https://www.google.com"

what = input("Search this: ")
driver = webdriver.Chrome(path)
driver.get(google)

# print(driver.title)
search = driver.find_element_by_name("q")
search.send_keys(what)
search.send_keys(Keys.RETURN)

time.sleep(10)
driver.quit()