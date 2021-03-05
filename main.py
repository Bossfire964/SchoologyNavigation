from selenium import webdriver
import os
import time
import sys
import tofile

tofile.makefile()

browser = webdriver.Chrome('/Users/luke/Documents/chromedriver')
browser.set_window_position(-10000,0)
browser.get('https://lms.fcps.org')
usernameBox = browser.find_elements_by_xpath('//*[@id="userNameInput"]')[0]
usernameBox.send_keys(sys.argv[1])
passwordBox = browser.find_elements_by_xpath('//*[@id="passwordInput"]')[0]
passwordBox.send_keys(sys.argv[2])
sign_in = browser.find_elements_by_xpath('//*[@id="submitButton"]')[0]
sign_in.click()
time.sleep(3)
upcoming_event = browser.find_elements_by_xpath('//*[@id="right-column-inner"]/div[2]/div/div')
assignments = []
linkassi = []
for item in upcoming_event:
	if item.get_attribute("class") == "upcoming-event course-event":
		assignments.append(item)
for item in assignments:
	linkassi.append(item.find_element_by_xpath('.//h4/span/a').get_attribute('href'))
for item in assignments:
	time.sleep(3)
	browser.get(linkassi[assignments.index(item)])
	try: 
		duedate = browser.find_elements_by_xpath('//*[@id="content-wrapper"]/div/div/div/div[3]/div/div/div/div/div/p/strong')[0].text
		desd = "No Description"
		try:
			desd = browser.find_elements_by_xpath('//*[@id="content-wrapper"]/div/div/div/div[3]/div/div/div/div/div/div/p')[0].text
		except:
			pass
		titletext = browser.find_elements_by_xpath('//*[@id="content-wrapper"]/div/div/div/div[2]/div/div/div[1]/h1')[0].text
		docbutton = browser.find_elements_by_xpath('//*[@id="content-wrapper"]/div/div/div/div[2]/div/div/div[1]/section/nav/div/button[2]')[0]
		docbutton.click()
		time.sleep(1)
		tofile.updateTypeOne('_'.join(titletext.split()), titletext, desd, duedate)
		browser.find_elements_by_xpath('//*[@id="header"]/header/nav/ul[1]/li[1]/a')[0].click()
		print("Proccesed " + titletext)
	except Exception as e:
		try:
			destable = []
			duedate = browser.find_element_by_xpath('//*[@id="main-inner"]/div[1]/p').text
			text = browser.find_elements_by_xpath('//*[@id="main-inner"]/div[2]/div/div/div')
			if len(text) == 0:
				text = browser.find_elements_by_xpath('//*[@id="main-inner"]/div[2]/div/div/p')
			for item in text:
				destable.append(item.text)
			title = browser.find_elements_by_xpath('//*[@id="center-top"]/h2')[0].text
			attachments = "No Attachments"
			try:
				attach = browser.find_elements_by_xpath('//*[@id="main-inner"]/div[3]/div')
				for item in attach:
					linkdoc = browser.find_elements_by_xpath('./div/span[1]/a')
					attachments = []
					attachments.append(linkdoc.get_attribute('href'))
			except:
				pass
			tofile.updateTypeTwo('_'.join(title.split()), title, duedate, destable, attachments)
			browser.find_elements_by_xpath('//*[@id="header"]/header/nav/ul[1]/li[1]/a')[0].click()
			print("Proccesed " + title)
		except Exception as e:
			raise e

tofile.finishFile()
browser.close()