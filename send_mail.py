# Script to send mail using yahoo.com
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.implicitly_wait(50)
driver.get('https://www.yahoo.com')

element = driver.find_element_by_xpath('//*[@id="header-signin-link"]')
element.click()

username = "abcd@yahoo.in"
password = "**********"
# Add your username and password here.
userid = driver.find_element_by_css_selector('#login-username')
userid.send_keys(username) 
driver.implicitly_wait(50)
nextpage = driver.find_element_by_xpath('//*[@id="login-signin"]')
nextpage.click()

passid = driver.find_element_by_xpath('//*[@id="login-passwd"]')
passid.send_keys(password)
driver.implicitly_wait(50)
nextpage1 = driver.find_element_by_xpath('//*[@id="login-signin"]')
nextpage1.click()
driver.implicitly_wait(50)
mail = driver.find_element_by_xpath('//*[@id="header-mail-button"]')
mail.click()
driver.implicitly_wait(100)
compose = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/nav/div/div[1]/a')
compose.click()

receivermail = "efgh@gmail.com"
# Add Receiver's mail id
receiver = driver.find_element_by_xpath('//*[@id="message-to-field"]')
receiver.send_keys(receivermail) 
driver.implicitly_wait(50)
sub = "Web Automation"
# Add subject of the mail
subject = driver.find_element_by_css_selector('#mail-app-component > div.p_a.R_0.T_0.L_0.B_0.D_F > div > div.compose-header.en_0 > div:nth-child(3) > div > div > input')
subject.send_keys(sub) 
driver.implicitly_wait(50)
send = driver.find_element_by_css_selector('#mail-app-component > div.p_a.R_0.T_0.L_0.B_0.D_F > div > div.em_N.D_F.ek_BB.p_R.o_h > div:nth-child(2) > div > button')
driver.implicitly_wait(50)
send.click() 
driver.close()