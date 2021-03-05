import os
import json

data = {}

def makefile():
	path = os.path.dirname(os.path.realpath(__file__)).split('/')
	path.pop(-1)
	path.append('Resources')
	path = '/'.join(path)
	f = open(path + "/S-Upcoming.json", 'w')
	f.close()
def addData(key, value, under):
	try:
		data[under][key] = value
	except:
		data[under] = {}
		data[under][key] = value
def finishFile():
	user = os.path.dirname(os.path.realpath(__file__)).split('/')[2]
	with open('/Users/' + user + '/Documents/Schoology.json', 'w') as f:
		json.dump(data, f, indent=2)
def updateTypeOne(under, title, des, due):
	addData('Title', title, under)
	addData('Description', des, under)
	addData('DueDate', due, under)
def updateTypeTwo(under, title, due, destable, attachments):
	addData('Title', title, under)
	addData('DueDate', due, under)
	addData('Description', destable, under)
	addData('Attachments', attachments, under)