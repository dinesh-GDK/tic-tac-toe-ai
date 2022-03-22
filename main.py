from orchestrator import Orchestrator
from human import Human
from randomBot import RandomBot
from superBot import SuperBot

# TODO
# color terminal output
# docstring

if __name__ == "__main__":

	player1 = SuperBot("X")
	player2 = RandomBot("O")
	# player2 = Human("X")
	orch = Orchestrator(player1, player2)
	orch.run()
