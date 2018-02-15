"""Reinforcement learning agent."""


import numpy as np
import json
import sys


class Agent(object):
    """Agent is the reinforcement learning agent that learns optimal state action pairs."""
    def __init__(self, game, qtable=dict(), player='X', learning_rate=5e-1, discount=1, epsilon=5e-1):
        """Initialize agent with properties

        - qtable is json table with Q values Q(s,a)
        - game is reference to game being played
        - player is what player the agent is 'X' or 'O'
        - learning_rate is alpha value for gradient update
        - discount is discount factor for future expected rewards
        - epsilon is probability of exploration in epsilon greedy strategy
        """
        self.game = game
        self.qtable = qtable
        self.player = player
        self.learning_rate = learning_rate
        self.discount = discount
        self.epsilon = epsilon

    def qvalue(self, state):
        """Retrieve value from qtable or initialize if not found."""
        if state not in self.qtable:
            # Initialize Q-value at 0
            self.qtable[state] = 0.0
        return self.qtable[state]

    def argmax(self, values):
        """Returns index of max value."""
        vmax = np.max(values)
        max_indices = []
        for i, v in enumerate(values):
            if v == vmax:
                max_indices.append(i)
        return np.random.choice(max_indices)

    def argmin(self, values):
        """Returns index of min value."""
        vmin = np.min(values)
        min_indices = []
        for i, v in enumerate(values):
            if v == vmin:
                min_indices.append(i)
        return np.random.choice(min_indices)

    def step(self, history=False, verbose=False):
        """Agent makes one step.

        - Deciding optimal or random action following e-greedy strategy given current state
        - Taking selected action and observing next state
        - Calculating immediate reward of taking action, current state, and next state
        - Updating q table values using GD with derivative of MSE of Q-value
        - Returns game status
        """
        state = self.game.get_state(self.game.board)
        action = self.next_move()
        winner = self.game.make_move(action)
        reward = self.reward(winner)
        self.update(reward, winner)
        if verbose:
            print("=========")
            print(state)
            print(action)
            print(winner)
            self.game.print_board()
            print(reward)
        return (winner, reward)

    def next_move(self):
        """Selects next move in MDP following e-greedy strategy."""
        states, actions = self.game.get_open_moves()
        # Exploit
        i = self.optimal_next(states)
        if np.random.random_sample() < self.epsilon:
            # Explore
            i = np.random.randint(0, len(states))
        return actions[i]

    def optimal_next(self, states):
        """Selects optimal next move.

        Input
        - states list of possible next states
        Output
        - index of next state that produces maximum value
        """
        values = [self.qvalue(s) for s in states]
        # Exploit
        if self.game.player == self.player:
            # Optimal move is max
            return self.argmax(values)
        else:
            # Optimal move is min
            return self.argmin(values)

    def reward(self, winner):
        """Calculates reward for different end game conditions.

        - win is 1.0
        - loss is -1.0
        - draw and unfinished is 0.0
        """
        opponent = 'O' if self.player == 'X' else 'X'
        if (winner == self.player):
            return 1.0
        elif (winner == opponent):
            return -1.0
        else:
            return 0

    def update(self, reward, winner):
        """Updates q-value.

        Update uses recorded observations of performing a
        certain action in a certain state and continuing optimally from there.
        """
        state = self.game.get_state(self.game.board)
        # Finding estimated future value by finding max(Q(s', a'))
        # If terminal condition is reached, future reward is 0
        future_val = 0
        if not winner:
            future_states, _ = self.game.get_open_moves()
            i = self.optimal_next(future_states)
            future_val = self.qvalue(future_states[i])
        # Q-value update
        self.qtable[state] = ((1 - self.learning_rate) * self.qvalue(state)) + (self.learning_rate * (reward + self.discount * future_val))

    def train(self, episodes, history=[]):
        """Trains by playing against self.

        Each episode is a full game
        """
        x = range(episodes)
        cumulative_reward = []
        memory = []

        total_reward = 0.0
        for i in range(episodes):
            game_active = True
            # First move is random to promote exploration
            _, actions = self.game.get_open_moves()
            winner = self.game.make_move(actions[np.random.randint(0, len(actions))])
            reward = self.reward(winner)
            total_reward += reward
            self.update(reward, winner)
            # Rest of game follows strategy
            while(game_active):
                winner, reward = self.step()
                total_reward += reward
                if winner:
                    game_active = False
                    self.game.reset()
            cumulative_reward.append(total_reward)
            memory.append(sys.getsizeof(self.qtable) / 1024)
            # Record total reward agent gains as training progresses
            if (i % (episodes / 10) == 0) and (i >= (episodes / 10)):
                print('.')
        # self.save_values()
        history.append(x)
        history.append(cumulative_reward)
        history.append(memory)
        return history

    def stats(self):
        """Agent plays optimally against self with no exploration.

        Records win/loss/draw distribution.
        """
        x_wins = 0
        o_wins = 0
        draws = 0
        episodes = 10000
        for i in range(episodes):
            game_active = True
            while(game_active):
                states, actions = self.game.get_open_moves()
                i = self.optimal_next(states)
                winner = self.game.make_move(actions[i])
                if winner:
                    if (winner == 'X'):
                        x_wins += 1
                    elif (winner == 'O'):
                        o_wins += 1
                    else:
                        draws += 1
                    game_active = False
                    self.game.reset()
        print('    X: {} Draw: {} O: {}'.format((x_wins * 1.0) / episodes,
                                                (draws * 1.0) / episodes,
                                                (o_wins * 1.0) / episodes))

    def save_values(self, path='data/qtable.json'):
        """Save Q values to json."""
        with open(path, 'w') as out:
            json.dump(self.qtable, out)

    def demo(self):
        """Demo so users can play against trained agent."""
        self.game.print_instructions()
        # Agent goes first
        game_active = True
        turn = 0
        while game_active:
            winner = None
            if turn == 0:
                states, actions = self.game.get_open_moves()
                i = self.optimal_next(states)
                winner = self.game.make_move(actions[i])
                self.game.print_board()
                turn = 1
            elif turn == 1:
                print('Select move:')
                p = int(sys.stdin.readline()[:-1])
                if self.game.is_valid_move(p):
                    winner = self.game.make_move(p)
                    self.game.print_board()
                    turn = 0
                else:
                    print('Invalid move.')
            if winner:
                print('Winner: {}'.format(winner))
                game_active = False
        self.game.reset()
