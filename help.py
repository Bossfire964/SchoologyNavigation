import sys
import os

if sys.argv[1] == "help":
	path = os.path.dirname(os.path.realpath(__file__)).split('/')
	with open('/'.join(path) + '/README.md', "r") as f:
		lines = f.readlines()
		for line in lines:
			print(line)