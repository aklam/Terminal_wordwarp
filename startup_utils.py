import os
import re
import sys
import copy
import time
import random
import string
import itertools

vowels = re.compile("a|e|i|o|u",re.IGNORECASE)
#get all possible combinations of the character list
def get_power_set(gen_chars, min_len):
	sorted_gen_chars = sorted(gen_chars)
	power_set=[[]]
	# iterate over the sub sets so far
	for elem in sorted_gen_chars:
		# add a new subset consisting of the subset at hand added elem
		for sub_set in power_set: 
			power_set=power_set+[list(sub_set)+[elem]]

	char_permutations = []
	for subset in power_set:
		subset_add = ''.join(subset)
		if len(subset_add) >= min_len and vowels.search(subset_add) != None:
			char_permutations.append(subset_add)
				
	return char_permutations

#generates the random characters to be used in the game
def gen_rand_chars(num_chars):
	words6_file = open("words6.txt","r")
	list_6_words = words6_file.read().split("\n")
	return list(random.choice(list_6_words))
	

#read all of the words in the word file
def read_words_file(words_filename):
	words_file = open(words_filename, "r")
	words = {}
	for line in words_file:
		if len(line) < 8 and len(line) > 3:
			words[line[:-1]] = 1
	return words

#find all the possible words that can be made using the combinations
#of the random characters
def possible_words(words, char_list):
	char_list_power = get_power_set(char_list,3)

	letters_to_words = {}
	has_max_len_word = False
	for word in words:
		word_sorted = ''.join(sorted(word))
		if word_sorted not in letters_to_words:
			letters_to_words[word_sorted] = []
		letters_to_words[word_sorted].append(word)

	rand_possible_words = {}
	for subset in char_list_power:
		if subset in letters_to_words:
			for w in letters_to_words[subset]:
				rand_possible_words[w] = 0
				if len(w) == 6:
					has_max_len_word = True

	return rand_possible_words if has_max_len_word else {}
