import os
import sys
from bs4 import BeautifulSoup

def get_word_definitions(dev=False):
	path_to_defs = os.getcwd() + '/words_and_defs/'
	all_def_files = os.listdir(path_to_defs)
	win_rows, win_columns = os.popen('stty size', 'r').read().split()
	bar_width = int(win_columns) - 20

	word_definitions = {}

	for def_file in all_def_files:
		if not def_file.endswith('.html') or def_file == "index.html":
			continue
		if dev:
			print(def_file)
		defs = open(path_to_defs + def_file,encoding='iso-8859-15')
		soup = BeautifulSoup(defs,"lxml") 
		word_defs_html = soup.body.find_all("p")

		for entry in word_defs_html:
			word_lower = entry.b.string.lower()
			if word_lower not in word_definitions:
				word_definitions[word_lower] = []
			if entry.contents[3][2:] not in word_definitions[word_lower]:
				word_definitions[word_lower].append(entry.contents[3][2:])

	word_defs_condensed = {}
	for word in word_definitions:
		word_def_cond = ""
		if len(word_definitions[word]) > 1:
			i = 1
			for definition in word_definitions[word]:
				word_def_cond += "("+str(i)+") " + definition + "\n"
				i += 1
				if i > 4:
					break
		else:
			word_def_cond += definition + "\n"
		word_defs_condensed[word] = word_def_cond

	return word_defs_condensed


