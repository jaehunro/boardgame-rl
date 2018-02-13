"""Test suite for Reinforcement Learning Agent.

To run:
    python -m unittest -v tests.rl.test_agent.py

"""


import unittest
from game.tictactoe import TicTacToe
from rl.agent import Agent


class TestAgent(unittest.TestCase):
    """Collection of unittests for RL Agent."""

    def setUp(self):
        """Initialize RL Agent."""
        game = TicTacToe()
        self.agent = Agent(game)

    def tearDown(self):
        """Reinitialize RL Agent."""
        game = TicTacToe()
        self.agent = Agent(game)

    def test_qvalue(self):
        """Test qvalue to init to 0 if not present and return value else wise."""
        state = '---------'
        self.assertEqual(0.0, self.agent.qvalue(state))
        self.agent.qtable[state] = 1.0
        self.assertEqual(1.0, self.agent.qvalue(state))

    def test_argmax(self):
        """Test argmax with values list."""
        values = [0, 1, 5, 3, 4]
        self.assertEqual(2, self.agent.argmax(values))

    def test_argmin(self):
        """Test argmin with values list."""
        values = [0, 1, 5, -1, 4]
        self.assertEqual(3, self.agent.argmin(values))

    def test_reward(self):
        """Test reward with different winners."""
        self.agent.player = 'X'
        self.assertEqual(1.0, self.agent.reward(winner='X'))
        self.assertEqual(-1.0, self.agent.reward(winner='O'))
        self.assertEqual(0.0, self.agent.reward(winner='Draw'))
        self.assertEqual(0.0, self.agent.reward(winner=None))


if __name__ == '__main__':
    unittest.main()
