from color import color
from orchestrator import Orchestrator
from human import Human
from randomBot import RandomBot
from superBot import SuperBot

def get_player(marker):

	entry = True
	ip = -1

	while ip < 1 or ip > 3 or entry:
		
		if not entry:
			print("Wrong input")

		entry = False

		try:
			ip = int(input(f"Enter Player {color[marker]}: "))
		except ValueError:
			continue

	player = None

	if ip == 1:
		player = Human(marker)
	elif ip == 2:
		player = RandomBot(marker)
	else:
		player = SuperBot(marker)
	
	return player

if __name__ == "__main__":

	print(f"Choose Player {color['X']} and Player {color['O']}")
	print("Option 1 - Human")
	print("Option 2 - Random Bot")
	print("Option 3 - Super Bot\n")
		
	player1 = get_player("X")
	player2 = get_player("O")

	orch = Orchestrator(player1, player2)
	orch.run()
