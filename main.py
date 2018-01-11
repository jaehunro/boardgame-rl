from rl.tictactoe import *
from rl.agent import *

if __name__ == '__main__':
	game = TicTacToe()
	# game.print_board()
	qtable = json.load(open('data/qtable.json'))
	agent = Agent(game)
	print "Before Training"
	agent.demo()

	agent.train(1000)
	print "After 1000 Episodes"
	agent.stats()
	agent.demo()

	agent.train(4000)
	print "After 5000 Episodes"
	agent.stats()
	agent.demo()

	agent.train(5000)
	print "After 10000 Episodes"
	agent.stats()
	agent.demo()

	agent.train(20000)
	print "After 30000 Episodes"
	agent.stats();
	agent.demo();