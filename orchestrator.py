from board import Board

class Orchestrator:

	def __init__(self, player1, player2):

		assert(player1.marker != player2.marker)
		
		self._player1 = player1
		self._player2 = player2
		self._board = Board()

	def run(self):
		
		winner = None
		self._board.print()

		while True:
			
			row, col = self._player1.play(self._board.state())
			self._board.update(row, col, self._player1.marker)
			self._board.print()

			winner = self._board.check()
			if winner != None:
				break

			row, col = self._player2.play(self._board.state())
			self._board.update(row, col, self._player2.marker)
			self._board.print()

			winner = self._board.check()
			if winner != None:
				break

		if winner == "T":
			print("It's a Tie")
		else:
			print(f"Player {self._board.check()} won")
