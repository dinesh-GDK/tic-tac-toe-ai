class Human():

	def __init__(self, marker):
		self.marker = marker

	def play(self, state):

		row, col = -1, -1
		entry = True

		while (row < 0 or row > 2 or col < 0 or col > 2) or state[row][col] != " ":

			if not entry:
				print("Wrong inputs!")
			
			entry = False

			try:
				pos = int(input("Your turn, Enter position: "))
			except ValueError:
				pass

			row = (pos-1) // 3
			col = (pos-1) % 3
		
		return row, col
