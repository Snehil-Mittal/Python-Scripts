# Script to open Facebook and login into your Facebook account automatically
from selenium import webdriver
# webdriver is needed when you need to operate on browser
from selenium.webdriver.common.keys import Keys
user_name = "abcd@yahoo.in"
# Add your username here.
password = "**********"
# Add your password here.
driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
element = driver.find_element_by_id("email")
element.send_keys(user_name)
# send_keys is like typing or writing on the screen
element = driver.find_element_by_id("pass")
element.send_keys(password)
element.send_keys(Keys.RETURN)
# Keys.RETURN is the way of pressing enter key