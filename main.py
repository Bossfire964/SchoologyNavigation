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

