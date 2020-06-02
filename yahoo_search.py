# Script to open yahoo.com and search a word on it.
from selenium import webdriver
# webdriver is needed when you need to operate on browser
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
# Here I am using Chrome Web browser and therefore including its wed driver
# You can use Mozilla Firefox also and for that gecko driver is required
driver.get('https://www.yahoo.com')
# This get() function is used to open the entered url
searchbox = driver.find_element_by_xpath('//*[@id="header-search-input"]')
searchbox.send_keys("Hello")
# Enter your search word here.
element = driver.find_element_by_xpath('//*[@id="header-desktop-search-button"]')
element.click()

