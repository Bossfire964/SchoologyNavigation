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
linkassi = []
for item in upcoming_event:
	if item.get_attribute("class") == "upcoming-event course-event":
		assignments.append(item)
print(len(assignments))
for item in assignments:
	linkassi.append(item.find_element_by_xpath('.//h4/span/a').get_attribute('href'))
for item in assignments:
	time.sleep(3)
	browser.get(linkassi[assignments.index(item)])
	try: 
		print(browser.find_elements_by_xpath('//*[@id="content-wrapper"]/div/div/div/div[3]/div/div/div/div/div/p/strong')[0].text)
		try:
			print(browser.find_elements_by_xpath('//*[@id="content-wrapper"]/div/div/div/div[3]/div/div/div/div/div/div/p')[0].text)
		except:
			pass
		docbutton = browser.find_elements_by_xpath('//*[@id="content-wrapper"]/div/div/div/div[2]/div/div/div[1]/section/nav/div/button[2]')[0]
		docbutton.click()
		time.sleep(2)
		browser.find_elements_by_xpath('//*[@id="header"]/header/nav/ul[1]/li[1]/a')[0].click()
	except Exception as e:
		print(e)
		try:
			print(browser.find_element_by_xpath('//*[@id="main-inner"]/div[1]/p').text)
			text = browser.find_elements_by_xpath('//*[@id="main-inner"]/div[2]/div/div/div')
			if len(text) == 0:
				text = browser.find_elements_by_xpath('//*[@id="main-inner"]/div[2]/div/div/p')
			for item in text:
				print(item.text)
			title = browser.find_elements_by_xpath('//*[@id="center-top"]/h2')[0].text
			try:
				attach = browser.find_elements_by_xpath('//*[@id="main-inner"]/div[3]/div')
				for item in attach:
					linkdoc = browser.find_elements_by_xpath('./div/span[1]/a')
					links = linkdoc.get_attribute('href')
			except:
				pass
			browser.find_elements_by_xpath('//*[@id="header"]/header/nav/ul[1]/li[1]/a')[0].click()
		except Exception as e:
			raise e