import os
import re
import sys
import csv
import time
import math
import string
from startup_utils import *
from game_params import *

#read all of the words in the word file
def find_6words(all_words, num_chars=6, min_words=12):
	words6_file = open("words"+str(num_chars)+".txt","w")
	win_rows, win_columns = os.popen('stty size', 'r').read().split()
	bar_width = int(win_columns) - 20
	num_words = len(all_words)
	load_bar_unit = int(num_words/bar_width)
	print("This will take ~5 min")
	print(bcolors.BOLD + "-"*math.ceil((bar_width-7)/2) + "Loading" + "-"*math.ceil((bar_width-7)/2) + bcolors.ENDC)
	i = 0
	for word in all_words:
		i += 1
		if len(word)==num_chars:
			char_set = list(word)
			char_permute = get_power_set(char_set,4)
			pos_words = possible_words(all_words, char_set)
			num_possible = len(pos_words)
			if  num_possible > min_words:
				words6_file.write(word+"\n")
		##loading bar, dw about it
		if i % load_bar_unit == 0: 
			num_units = int(i/load_bar_unit)
			sys.stdout.write("\r" + bcolors.BOLD + "<" + bcolors.OKGREEN + "#"*num_units + bcolors.ENDC + bcolors.FAIL + "="*(bar_width-num_units)+ bcolors.ENDC + bcolors.BOLD + ">" + bcolors.ENDC + " "*8)
		if i > load_bar_unit and (i % 50 == 0 or i % load_bar_unit == 0):
			sys.stdout.write("\b"*8 + bcolors.BOLD + "\t{0:.2f}%".format(100*i/num_words) + bcolors.ENDC)
			sys.stdout.flush()
	sys.stdout.flush("\n")


#http://www.kilgarriff.co.uk/bnc-readme.html#lemmatised
def process_kilgarriff_words(names_dict):
	freq_file  = open("all.num","r") 

	proc_words_file = open("words_filter.txt","w")
	for line in freq_file:
		word_att = line.split()
		if word_att[1].isalpha() and word_att[1].islower() and int(word_att[0]) >= 10 and word_att[1] not in names_dict:
			proc_words_file.write(word_att[1] + "\n")

def process_names():
	all_names = {}
	names_file = open("yob2017.txt","r")
	names_csv  = csv.reader(names_file,delimiter=",")
	for line in names_csv:
		all_names[line[0].lower()] = 1
	return all_names