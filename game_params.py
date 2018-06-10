import sys
import copy
import time
import random
import string
import itertools

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Game_params:
	def __init__(self,rand_characters,valid_words,valid_char_subsets):
		self.rand_characters    = sorted(rand_characters)

		self.num_chars          = len(rand_characters)

		self.valid_words        = valid_words
		self.sorted_len_words   = sorted(valid_words.keys(),key=len)
		self.valid_char_subsets = valid_char_subsets
		self.guesses_tried      = {}

		self.total_num_words    = 0
		self.num_words_guessed  = 0

		self.score              = 0
		self.max_score          = 0
		for word in valid_words:
			self.total_num_words += 1
			self.max_score += len(word) * 10

	def valid_guess(self, guess):
		if guess not in self.guesses_tried:
			self.guesses_tried[guess] = 1
		else:
			self.guesses_tried[guess] += 1

		if guess in self.valid_words:
			if self.valid_words[guess] == 0:
				self.num_words_guessed += 1
				self.score += len(guess) * 10
			self.valid_words[guess] += 1
			return True
		return False

	def guess_history(self):
		for guess in self.guesses_tried:
			print(guess + ": " + str(self.guesses_tried[guess]))
		return

	def game_num_chars(self):
		return self.num_chars

	def char_set(self):
		ret = self.rand_characters[0]
		for i in range(len(self.rand_characters)-1):
			ret += " " + self.rand_characters[i+1]
		return ret

	def shuffle_char_set(self):
		random.shuffle(self.rand_characters)

	def draw_progress(self):
		i = 0
		print(bcolors.BOLD + "Words guessed: " + str(self.num_words_guessed)+"/"+str(self.total_num_words))
		print("        Score: " + str(self.score)+"/"+str(self.max_score))
		for word in self.sorted_len_words:
			if i % 10 == 0 and i != 0:
				print("\n")
			if self.valid_words[word] == 0:
				print(bcolors.FAIL + "_"*len(word) + "\t" + bcolors.ENDC,end='')
			else:
				print(bcolors.OKGREEN + bcolors.UNDERLINE + word + "\t" + bcolors.ENDC,end='')
			i += 1
		print("\n", end='')

	def give_up(self):
		i = 0
		for word in self.sorted_len_words:
			if i % 10 == 0 and i != 0:
				print("\n")
			if self.valid_words[word] == 0:
				print(bcolors.FAIL + word + "\t" + bcolors.ENDC,end='')
			else:
				print(bcolors.OKGREEN + word + "\t" + bcolors.ENDC,end='')
			i += 1
		print("\n", end='')

