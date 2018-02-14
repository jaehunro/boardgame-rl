"""Train and demo Reinforcement Learning agent.

To run:
    python main.py

"""


import argparse
import sys
import matplotlib.pyplot as plt
import ujson as json

from game.tictactoe import TicTacToe
from game.connectfour import ConnectFour
from rl.agent import Agent


def process_args():
    """Process command line args."""
    message = 'Interactive Reinforcement Learning board game playing agent.'
    parser = argparse.ArgumentParser(description=message)

    default_game = 'tictactoe'
    default_mode = 'train'

    parser.add_argument('-g', '--game',
                        dest='game',
                        help='Board game choice.',
                        default=default_game)

    parser.add_argument('-m', '--mode',
                        dest='mode',
                        help='Mode for Agent can be train or demo.',
                        default=default_mode)

    options = parser.parse_args()
    return options


def play_tictactoe(mode):
    """Start TicTacToe game with RL Agent."""
    print('==TIC TAC TOE==')
    game = TicTacToe()

    if mode == 'train':
        agent = Agent(game)
        history = agent.train(10000)
        print('After 10000 Episodes')
        fig, ax = plt.subplots()
        ax.plot(history[0][:100], history[1][:100])

        ax.set(xlabel='Episode', ylabel='Cumulative Reward',
               title='Tic Tac Toe Agent 100 Episodes')
        ax.grid()
        fig.savefig('img/tictactoe_100.png')

        ax.plot(history[0][:1000], history[1][:1000])

        ax.set(xlabel='Episode', ylabel='Cumulative Reward',
               title='Tic Tac Toe Agent 1000 Episodes')
        fig.savefig('img/tictactoe_1000.png')

        ax.plot(history[0][:10000], history[1][:10000])

        ax.set(xlabel='Episode', ylabel='Cumulative Reward',
               title='Tic Tac Toe Agent 10000 Episodes')
        fig.savefig('img/tictactoe_10000.png')
        plt.show()

        agent.save_values(path='data/tictactoe_qtable.json')
        agent.stats()
        agent.demo()

    elif mode == 'demo':
        qtable = json.load(open('data/tictactoe_qtable.json'))
        agent = Agent(game, qtable=qtable)
        agent.demo()

    else:
        print('Mode {} is invalid.'.format(mode))


def play_connectfour(mode):
    """Start Connect Four game and training."""
    print('==CONNECT FOUR==')
    game = ConnectFour()

    if mode == 'train':
        agent = Agent(game)
        history = agent.train(10000)
        print('After 10000 Episodes')
        fig, ax = plt.subplots()
        ax.plot(history[0][:100], history[1][:100])

        ax.set(xlabel='Episode', ylabel='Cumulative Reward',
               title='Connect Four Agent 100 Episodes')
        ax.grid()
        fig.savefig('img/connectfour_100.png')

        ax.plot(history[0][:1000], history[1][:1000])

        ax.set(xlabel='Episode', ylabel='Cumulative Reward',
               title='Connect Four Agent 1000 Episodes')
        fig.savefig('img/connectfour_1000.png')

        ax.plot(history[0][:10000], history[1][:10000])

        ax.set(xlabel='Episode', ylabel='Cumulative Reward',
               title='Connect Four Agent 10000 Episodes')
        fig.savefig('img/connectfour_10000.png')
        plt.show()

        agent.save_values(path='data/connectfour_qtable.json')
        agent.demo()

    elif mode == 'demo':
        qtable = json.load(open('data/connectfour_qtable.json'))
        agent = Agent(game, qtable=qtable)
        agent = Agent(game)
        agent.demo()

    else:
        print('Mode {} is invalid.'.format(mode))


def main():
    """Entry point."""
    options = process_args()
    if options.game == 'tictactoe':
        play_tictactoe(options.mode)
    elif options.game == 'connectfour':
        play_connectfour(options.mode)
    else:
        print('Game choice {} is current unsupported.'
              .format(options.game))
        sys.exit(1)


if __name__ == '__main__':
    main()
