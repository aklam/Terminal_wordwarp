import os
import sys
import copy
import time
import random
import string
import itertools
from startup_utils import *
from game_params import *


def game_startup(all_words, num_play_chars, min_num_words, dev=False):
	
	rand_chars = gen_rand_chars(num_play_chars)
	num_char_sets = 1
	possible_words_from_chars = possible_words(all_words, rand_chars)

	
	while len(possible_words_from_chars) < min_num_words:
		num_char_sets += 1
		rand_chars = gen_rand_chars(num_play_chars)
		possible_words_from_chars = possible_words(all_words, rand_chars)

	valid_char_subsets = get_power_set(rand_chars,0)

	print("Game Size: " + str(num_play_chars))
	print("Number of Words: " +str(len(possible_words_from_chars)))
	if dev:
		print("Tried " + str(num_char_sets) + " character sets")
		print(possible_words_from_chars)
	return(Game_params(rand_chars, possible_words_from_chars,valid_char_subsets))

def game_round(ww_game,round_duration,dev=False):
	input("Press ENTER to continue")
	start_time = time.time()
	warning = ""
	while time.time()-start_time < round_duration:
		temp = os.system("clear")
		ww_game.draw_progress()
		print("Chararacter set: " + bcolors.BOLD + ww_game.char_set()+bcolors.ENDC)
		print(warning,end='')
		warning = ""
		query = input("Guess: ")
		if query == "":
			warning = "Please enter a guess or a command. Type HELP for help\n"
		elif query == "QUIT" or query == "Q":
			temp = os.system("clear")
			ww_game.give_up()
			print("Game Over")
			return(-1)
		elif query == "END ROUND":
			break
		elif query == "SHUFFLE" or query == "1":
			ww_game.shuffle_char_set()
		elif len(query) > ww_game.game_num_chars():
			warning = "Please only submit queries of length less than or equal to: " + str(ww_game.game_num_chars()) + "\n"
		elif ''.join(sorted(query)) not in ww_game.valid_char_subsets:
			warning = "Please only enter queries that contain characers from the available character set\n"
		else:
			ww_game.valid_guess(query)

	print(time.time()-start_time)
	return(ww_game.score)
	
def global_game(dev=False):
	if not dev:
		size_input      = input("Game Size: ") 
		while not size_input.isnumeric():
			print("Please only input numbers as game size: ")
			size_input = input("Game Size: ")

		num_words_input = input("Minimum number of words: ") 
		while not num_words_input.isnumeric():
			print("Please only input numbers for minimum number of words: ")
			num_words_input = input("Minimum number of words: ")

		round_len_input = input("Round duration (sec): ") 
		while not round_len_input.isnumeric():
			print("Please only input numbers for round duration: ")
			round_len_input = input("Round duration (sec): ")

	num_play_chars = 6 if dev else int(size_input)
	min_num_words  = 10 if dev else int(num_words_input)
	round_duration = 120 if dev else int(round_len_input)
	all_words = read_words_file("words_filter.txt")
	word_warp = game_startup(all_words, num_play_chars, min_num_words, dev)
	while game_round(word_warp,round_duration,dev) > 0:
		word_warp = game_startup(all_words, num_play_chars, min_num_words, rand, dev)

global_game(True) if len(sys.argv) > 1 and sys.argv[1] == "default" else global_game()



