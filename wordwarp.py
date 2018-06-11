import os
import sys
import copy
import time
import random
import string
import itertools
from game_params import *
from startup_utils import *
from process_word_files import *


def game_startup(all_words, num_play_chars, min_num_words, is_classic, min_word_len, dev=False):
	
	rand_chars = gen_rand_chars(num_play_chars)
	num_char_sets = 1
	possible_words_from_chars = possible_words(all_words, rand_chars)
	
	while len(possible_words_from_chars) < min_num_words:
		num_char_sets += 1
		rand_chars = gen_rand_chars(num_play_chars)
		possible_words_from_chars = possible_words(all_words, rand_chars)

	valid_char_subsets = get_power_set(rand_chars,min_word_len)
	if dev:
		print("Tried " + str(num_char_sets) + " character sets")
		print(possible_words_from_chars)
	return(Game_params(rand_chars, possible_words_from_chars,valid_char_subsets))

def game_round(ww_game, round_duration, dev=False):
	input("Press ENTER to continue")
	start_time = time.time()
	warning = ""
	while time.time()-start_time < round_duration:
		temp = os.system("clear")
		ww_game.draw_progress()
		print("Chararacter set: " + bcolors.BOLD + ww_game.char_set()+bcolors.ENDC)
		print(warning,end='')
		warning = ""
		query = input("Guess: " + bcolors.BOLD).lower()
		if query == "":
			ww_game.shuffle_char_set()
		elif query == "QUIT" or query == "q":
			if input("Are you sure you want quit? (y/n) " + bcolors.ENDC).lower() != "y":
				continue
			temp = os.system("clear")
			ww_game.give_up()
			print("Game Over")
			return(-1)
		elif query == "end round":
			temp = os.system("clear")
			if ww_game.score == 0:
				print("Game Over")
			ww_game.give_up()
			return(ww_game.score)			
		elif len(query) > ww_game.game_num_chars():
			warning = "Please only submit queries of length less than or equal to: " + str(ww_game.game_num_chars()) + "\n"
		elif ''.join(sorted(query)) not in ww_game.valid_char_subsets:
			warning = "Please only enter queries that contain characers from the available character set\n"
		else:
			ww_game.valid_guess(query)

	return(ww_game.score)
	
def global_game(is_classic, dev=False):
	if not is_classic:
		size_input      = input("Game Size: ") 
		while not size_input.isnumeric():
			print("Please only input numbers as game size: ")
			size_input = input("Game Size: ")

		min_word_len_input = input("Minimum word length: ") 
		while not size_input.isnumeric():
			print("Please only input numbers as minimum word length: ")
			min_word_len_input = input("Minimum word length: ")

		num_words_input = input("Minimum number of words: ") 
		while not num_words_input.isnumeric():
			print("Please only input numbers for minimum number of words: ")
			num_words_input = input("Minimum number of words: ")

		round_len_input = input("Round duration (sec): ") 
		while not round_len_input.isnumeric():
			print("Please only input numbers for round duration: ")
			round_len_input = input("Round duration (sec): ")

	num_play_chars = 6   if is_classic else int(size_input)
	min_word_len   = 3   if is_classic else int(min_word_len_input)
	min_num_words  = 10  if is_classic else int(num_words_input)
	round_duration = 120 if is_classic else int(round_len_input)


	sys.stdout.write(bcolors.BOLD + "          Game Type: ")
	if is_classic:
		sys.stdout.write("Classic\n")
	else:
		sys.stdout.write("Custom\n")
	print("          Game Size: " + str(num_play_chars))
	print("Minimum Word Length: " + str(min_word_len) + bcolors.ENDC)

	all_words = read_words_file("words_filter.txt")
	word_warp = game_startup(all_words, num_play_chars, min_num_words, is_classic, min_word_len)
	round_score = game_round(word_warp, round_duration, dev)
	while round_score > 0:
		word_warp = game_startup(all_words, num_play_chars, min_num_words, is_classic, min_word_len)
		round_score = game_round(word_warp, round_duration, dev)


use_names = False
freq_filter = 100
if not os.path.isfile("words_filter.txt"):
	all_names = process_names() if use_names else {}
	process_kilgarriff_words(all_names,freq_filter)
	all_words = read_words_file("words_filter.txt")
	find_6words(all_words)

game_mode = input("Play classic? (y/n) ").lower()
while game_mode != "y" and game_mode != "n" and game_mode != "":
	game_mode = input("Play classic? (y/n) ")

if game_mode == "y" or game_mode == "":
	global_game(True)
else:
	global_game(False)
sys.stdout.write(bcolors.ENDC)

