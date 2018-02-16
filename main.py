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

        # Plot Reward Stats
        rfig, raxs = plt.subplots(nrows=3, ncols=1)
        rax_reward1 = raxs[0]
        rax_reward1.grid()
        rax_reward2 = raxs[1]
        rax_reward2.grid()
        rax_reward3 = raxs[2]
        rax_reward3.grid()

        rax_reward1.plot(history[0][:100], history[1][:100])
        rax_reward1.set(ylabel='Cumulative Reward', title='Tic Tac Toe Cumulative Reward Episodes')

        rax_reward2.plot(history[0][:1000], history[1][:1000], color='g')
        rax_reward2.set(ylabel='Cumulative Reward')

        rax_reward3.plot(history[0][:10000], history[1][:10000], color='r')
        rax_reward3.set(xlabel='Episode', ylabel='Cumulative Reward')

        rfig.savefig('tictactoe_reward.png')

        # Plot Qtable Memory Usage Stats
        memfig, memaxs = plt.subplots(nrows=3, ncols=1)
        memax_reward1 = memaxs[0]
        memax_reward1.grid()
        memax_reward2 = memaxs[1]
        memax_reward2.grid()
        memax_reward3 = memaxs[2]
        memax_reward3.grid()

        memax_reward1.plot(history[0][:100], history[2][:100])
        memax_reward1.set(ylabel='Size (KB)', title='Tic Tac Toe QTable Size Episodes')

        memax_reward2.plot(history[0][:1000], history[2][:1000], color='g')
        memax_reward2.set(ylabel='Size (KB)')

        memax_reward3.plot(history[0][:10000], history[2][:10000], color='r')
        memax_reward3.set(xlabel='Episode', ylabel='Size (KB)')

        memfig.savefig('tictactoe_memory.png')
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

        # Plot Reward Stats
        rfig, raxs = plt.subplots(nrows=3, ncols=1)
        rax_reward1 = raxs[0]
        rax_reward1.grid()
        rax_reward2 = raxs[1]
        rax_reward2.grid()
        rax_reward3 = raxs[2]
        rax_reward3.grid()

        rax_reward1.plot(history[0][:100], history[1][:100])
        rax_reward1.set(ylabel='Cumulative Reward', title='Connect Four Cumulative Reward (3 Column State)')

        rax_reward2.plot(history[0][:1000], history[1][:1000], color='g')
        rax_reward2.set(ylabel='Cumulative Reward')

        rax_reward3.plot(history[0][:10000], history[1][:10000], color='r')
        rax_reward3.set(xlabel='Episode', ylabel='Cumulative Reward')

        rfig.savefig('connectfour_reward.png')

        # Plot Qtable Memory Usage Stats
        memfig, memaxs = plt.subplots(nrows=3, ncols=1)
        memax_reward1 = memaxs[0]
        memax_reward1.grid()
        memax_reward2 = memaxs[1]
        memax_reward2.grid()
        memax_reward3 = memaxs[2]
        memax_reward3.grid()

        memax_reward1.plot(history[0][:100], history[2][:100])
        memax_reward1.set(ylabel='Size (KB)', title='Connect Four QTable Size (3 Column State)')

        memax_reward2.plot(history[0][:1000], history[2][:1000], color='g')
        memax_reward2.set(ylabel='Size (KB)')

        memax_reward3.plot(history[0][:10000], history[2][:10000], color='r')
        memax_reward3.set(xlabel='Episode', ylabel='Size (KB)')

        memfig.savefig('connectfour_memory.png')
        plt.show()

        agent.save_values(path='data/connectfour_qtable.json')
        agent.demo()

    elif mode == 'demo':
        qtable = json.load(open('data/connectfour_qtable.json'))
        agent = Agent(game, qtable=qtable)
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
