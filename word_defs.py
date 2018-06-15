import os
import glob
from bs4 import BeautifulSoup

def get_word_definitions():
	path_to_defs = os.getcwd() + '/OPTED/v003/'
	all_def_files = os.listdir(path_to_defs)[1:]

	word_defs = {}

	for def_file in all_def_files:
		print(def_file)
		defs = open(path_to_defs + def_file,encoding='iso-8859-15')
		soup = BeautifulSoup(defs,"lxml") 
		word_defs_html = soup.body.find_all("p")

		for entry in word_defs_html:
			word_lower = entry.b.string.lower()
			if word_lower not in word_defs:
				word_defs[word_lower] = entry.contents[3][2:]

	return word_defs


print(get_word_definitions()["ours"])