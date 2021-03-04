from selenium import webdriver
import os
import time
import sys


browser = webdriver.Chrome('/Users/luke/Documents/chromedriver')
browser.get('https://lms.fcps.org')
usernameBox = browser.find_elements_by_xpath('//*[@id="userNameInput"]')[0]
usernameBox.send_keys(sys.argv[1])
passwordBox = browser.find_elements_by_xpath('//*[@id="passwordInput"]')[0]
passwordBox.send_keys(sys.argv[2])
sign_in = browser.find_elements_by_xpath('//*[@id="submitButton"]')[0]
sign_in.click()
time.sleep(5)
upcoming_event = browser.find_elements_by_xpath('//*[@id="right-column-inner"]/div[2]/div/div')
assignments = []
for item in upcoming_event:
	if item.get_attribute("class") == "upcoming-event course-event":
		assignments.append(item)
print(len(assignments))
for item in assignments:
	link = item.find_element_by_xpath('.//h4/span/a')
	print(link.get_attribute('href'))
