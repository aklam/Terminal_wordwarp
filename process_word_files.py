import os
import re
import sys
import csv
import time
import string
from startup_utils import *


#read all of the words in the word file
def find_6words(all_words, num_chars=6, min_words=12):
	words6_file = open("words"+str(num_chars)+".txt","w")	
	for word in all_words:
		if len(word)==num_chars:
			char_set = list(word)
			char_permute = get_power_set(char_set,4)
			pos_words = possible_words(all_words, char_set)
			num_possible = len(pos_words)
			if  num_possible > min_words:
				print(word + " " + str(num_possible))
				words6_file.write(word+"\n")


#http://www.kilgarriff.co.uk/bnc-readme.html#lemmatised
def process_kilgarriff_words(names_dict):
	freq_file  = open("all.num","r")

	proc_words_file = open("words_filter.txt","w")
	for line in freq_file:
		word_att = line.split()
		if word_att[1].isalpha() and word_att[1].islower() and int(word_att[0]) >= 50 and word_att[1] not in names_dict:
			proc_words_file.write(word_att[1] + "\n")

def process_names():
	all_names = {}
	names_file = open("yob2017.txt","r")
	names_csv  = csv.reader(names_file,delimiter=",")
	for line in names_csv:
		all_names[line[0].lower()] = 1
	return all_names

all_names = process_names()
process_kilgarriff_words(all_names)
all_words = read_words_file("words_filter.txt")
find_6words(all_words)