import random

class RandomBot:
	
	def __init__(self, marker):
		self.marker = marker

	def play(self, state):

		row, col = -1, -1
		entry = True

		while state[row][col] != " " or entry:

			row = random.randint(0, 2)
			col = random.randint(0, 2)

			entry = False

		return row, col
