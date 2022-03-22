class Board:

	def __init__(self):

		self._state = [
			[" ", " ", " "],
			[" ", " ", " "],
			[" ", " ", " "]
		]

		self._limit = len(self._state)

	def state(self):
		return self._state

	def update(self, row, col, player):

		assert(player == "X" or player == "O")
		assert(row >= 0 and row < 3 and col >= 0 and col < 3)

		self._state[row][col] = player
		return self.check()

	def check(self):

		for i in range(self._limit):
			if self._state[i][0] == self._state[i][1] and \
				self._state[i][0] == self._state[i][2] and self._state[i][0] != " ":
				return self._state[i][0]

		for i in range(self._limit):
			if self._state[0][i] == self._state[1][i] and \
				self._state[0][i] == self._state[2][i] and self._state[0][i] != " ":
				return self._state[0][i]

		if self._state[0][0] == self._state[1][1] and \
			self._state[0][0] == self._state[2][2] and self._state[0][0] != " ":
			return self._state[0][0]

		if self._state[0][2] == self._state[1][1] and \
			self._state[0][2] == self._state[2][0] and self._state[0][2] != " ":
			return self._state[0][2]

		empty_state = 0
		for i in range(self._limit):
			for j in range(self._limit):
				if self._state[i][j] == " ":
					empty_state += 1

		if empty_state == 0:
			return "T"

		return None

	def print(self):

		print_state = [
			[" ", " ", " "],
			[" ", " ", " "],
			[" ", " ", " "]
		]

		for i in range(self._limit):
			for j in range(self._limit):
				if self._state[i][j] == " ":
					print_state[i][j] = i*self._limit + (j+1)
				else:
					print_state[i][j] = self._state[i][j]

		print()
		print(f"{print_state[0][0]} | {print_state[0][1]} | {print_state[0][2]}")
		print(f"---------")
		print(f"{print_state[1][0]} | {print_state[1][1]} | {print_state[1][2]}")
		print(f"---------")
		print(f"{print_state[2][0]} | {print_state[2][1]} | {print_state[2][2]}")
		print()
