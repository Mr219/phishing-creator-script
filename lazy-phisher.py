import os
import random
import requests
from data import colors
from data import header
def lazy_phisher():
	lazy_1 = colors.color.blue+"lazy@phisher"+colors.color.end
	lazy_1 += ":"
	lazy_1 += "8~> "
	lazyphisher = raw_input(lazy_1)

	if lazyphisher == "help" or lazyphisher == "h":
		from data import help
		os.system("python data.py")

	elif lazyphisher == "creator":
		from data import creator
		os.system("python data.py")

	elif lazyphisher == "use":
		print ("["+colors.color.red+"Error"+colors.color.end+"] use with creator-name")
		lazy_phisher()

	elif lazyphisher == "clear":
		os.system("clear")
		lazy_phisher()

	elif lazyphisher == "about":
		from data import about
		os.system("python data.py")

	elif lazyphisher == "exit":
		os.system("clear")
		from data import exit

	elif lazyphisher == "use guide":
		from data import guide
		os.system("python data.py")

	elif lazyphisher == "use gmail":
		from data import gmail
		os.system("python data.py")

	elif lazyphisher == "use clone":
		from data import clone
		os.system("python data.py")

	elif lazyphisher == "use facebook":
		from data import facebook
		os.system("python data.py")

	elif lazyphisher == "use facebook_downloader":
		from data import downloader
		os.system("python data.py")

	elif lazyphisher == "use facebook_autofollower":
		from data import autofollower
		os.system("python data.py")

	elif lazyphisher == "use dota2":
		from data import dota2
		os.system("python data.py")


	else:
		os.system(lazyphisher)
		lazy_phisher()
lazy_phisher()
