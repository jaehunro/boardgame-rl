"""Train and demo Reinforcement Learning agent.

To run:
    python main.py

"""


import argparse
import sys

from game.tictactoe import TicTacToe
from game.connectfour import ConnectFour
from rl.agent import Agent


def process_args():
    """Process command line args."""
    message = 'Interactive Reinforcement Learning board game playing agent.'
    parser = argparse.ArgumentParser(description=message)

    default_game = 'tictactoe'

    parser.add_argument('-game', '--game',
                        dest='game',
                        help='Board game choice.',
                        default=default_game)

    options = parser.parse_args()
    return options


def play_tictactoe():
    """Start TicTacToe game with RL Agent."""
    print('==TIC TAC TOE==')
    game = TicTacToe()
    agent = Agent(game)
    print('Before Training')
    agent.demo()

    agent.train(1000)
    print('After 1000 Episodes')
    agent.stats()
    agent.demo()

    agent.train(4000)
    print('After 5000 Episodes')
    agent.stats()
    agent.demo()

    agent.train(5000)
    print('After 10000 Episodes')
    agent.stats()
    agent.demo()

    agent.train(20000)
    print('After 30000 Episodes')
    agent.stats()
    agent.demo()


def play_connectfour():
    """Start Connect Four game and training."""
    print('==CONNECT FOUR==')
    game = ConnectFour()
    agent = Agent(game)
    print('Before Training')
    agent.demo()

    agent.train(1000)
    print('After 1000 Episodes')
    agent.stats()
    agent.demo()

    agent.train(4000)
    print('After 5000 Episodes')
    agent.stats()
    agent.demo()

    agent.train(5000)
    print('After 10000 Episodes')
    agent.stats()
    agent.demo()

    agent.train(20000)
    print('After 30000 Episodes')
    agent.stats()
    agent.demo()


def main():
    """Entry point."""
    options = process_args()
    if options.game == 'tictactoe':
        play_tictactoe()
    elif options.game == 'connectfour':
        play_connectfour()
    else:
        print('Game choice {} is current unsupported.'
              .format(options.game))
        sys.exit(1)


if __name__ == '__main__':
    main()
