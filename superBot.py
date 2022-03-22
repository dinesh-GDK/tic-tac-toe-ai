class SuperBot:

	def __init__(self, marker):
		self.marker = marker
		self.emarker = "X" if marker == "O" else "O"
		self._limit = 3

		self.base = {
			self.marker: 1,
			self.emarker: -1, 
			"T": 0
		}

	def play(self, board):

		bestValue = float("-inf")
		x, y = -1, -1

		for i in range(3):
			for j in range(3):
				
				if board[i][j] != " ":
					continue

				board[i][j] = self.marker
				value = self.minimax(board, False)
				board[i][j] = " "

				if value > bestValue:
					bestValue = value
					x, y = i, j

		return x, y

	def minimax(self, board, isMaxPlayer):
		
		base = self.check(board)
		if base != None:
			return self.base[base]

		if isMaxPlayer:

			bestValue = float("-inf")

			for i in range(3):
				for j in range(3):
					
					if board[i][j] != " ":
						continue

					board[i][j] = self.marker
					value = self.minimax(board, False)
					board[i][j] = " "
					bestValue = max(bestValue, value)

			return bestValue

		else:

			bestValue = float("inf")

			for i in range(3):
				for j in range(3):
					
					if board[i][j] != " ":
						continue

					board[i][j] = self.emarker
					value = self.minimax(board, True)
					board[i][j] = " "
					bestValue = min(bestValue, value)

			return bestValue

	def check(self, board):

		for i in range(self._limit):
			if board[i][0] == board[i][1] and \
				board[i][0] == board[i][2] and board[i][0] != " ":
				return board[i][0]

		for i in range(self._limit):
			if board[0][i] == board[1][i] and \
				board[0][i] == board[2][i] and board[0][i] != " ":
				return board[0][i]

		if board[0][0] == board[1][1] and \
			board[0][0] == board[2][2] and board[0][0] != " ":
			return board[0][0]

		if board[0][2] == board[1][1] and \
			board[0][2] == board[2][0] and board[0][2] != " ":
			return board[0][2]

		empty_state = 0
		for i in range(self._limit):
			for j in range(self._limit):
				if board[i][j] == " ":
					empty_state += 1

		if empty_state == 0:
			return "T"

		return None
