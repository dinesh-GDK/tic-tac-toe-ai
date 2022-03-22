from color import color
class Human():

	def __init__(self, marker):
		self.marker = marker

	def play(self, state):

		row, col = -1, -1
		entry = True

		while (row < 0 or row > 2 or col < 0 or col > 2) or state[row][col] != " ":

			if not entry:
				print("Wrong location!")
			
			entry = False

			try:
				pos = int(input(f"Enter position: "))
			except ValueError:
				continue

			row = (pos-1) // 3
			col = (pos-1) % 3
		
		return row, col
