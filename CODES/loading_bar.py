import os
import sys
import math
import time
from game_params import *

class LoadingBar:
	def __init__(self):
		self.percent_complete = 0

		win_rows, win_columns = os.popen('stty size', 'r').read().split()
		self.bar_width    = int(win_columns) - 20
		self.bar_progress = 0
		print(bcolors.BOLD + "-"*math.ceil((self.bar_width-6)/2) + "Loading" + "-"*math.ceil((self.bar_width-6)/2) + bcolors.ENDC)
		self.draw_LoadingBar()

	def draw_LoadingBar(self):
		sys.stdout.write("\r" + bcolors.BOLD + "<" + bcolors.OKGREEN + "#"*self.bar_progress + bcolors.ENDC + bcolors.FAIL + "="*(self.bar_width-self.bar_progress) + bcolors.ENDC + bcolors.BOLD + ">" + bcolors.ENDC + " "*8)
		self.draw_percent_complete()

	def draw_percent_complete(self):
		sys.stdout.write("\b"*8 + bcolors.BOLD + "\t{0:.2f}%".format(self.percent_complete) + bcolors.ENDC)
		sys.stdout.flush()

	def add_progress_unit(self):
		self.bar_progress += 1
		self.draw_LoadingBar()

	def update_percentage(self):
		self.percent_complete += 1.0111
		self.draw_percent_complete()