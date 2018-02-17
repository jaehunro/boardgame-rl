"""Chomp."""


from game import Game
import sys


class Chomp(Game):
    """Chomp game class."""

    def __init__(self, rows=3, cols=4):
        """Construct new chomp game instance."""
        self.rows = rows
        self.cols = cols
        self.board = self.create_board(rows, cols)
        self.player = 'X'
        self.winner = None

    def create_board(self, rows, cols):
        """Create board given dimensions."""
        board = []
        for i in range(rows):
            board.append([])
            for j in range(cols):
                board[i].append('-')
        # Place poison in bottom left corner
        board[rows - 1][0] = 'P'
        return board

    def reset(self):
        """Reset game."""
        self.board = self.create_board(self.rows, self.cols)
        self.player = 'X'
        self.winner = None

    def flatten(self, board):
        """Returns flattened representation of board."""
        flattened = []
        for row in board:
            for val in row:
                flattened.append(val)
        return flattened

    def chomp(self, action, value):
        """Chomps out from board given action.

        Action is position and chomps all squares above and to the right of position.
        Value is either X, O or -
        """
        board = [row[:] for row in self.board]
        for i in range(self.rows):
            for j in range(self.cols):
                if i <= action[0] and j >= action[1]:
                    # Is above and to right of action position
                    if board[i][j] == '-':
                        # Is an empty space
                        board[i][j] = value + str(action[0]) + str(action[1])
        return board

    def get_state(self, board):
        """Get state representation of board."""
        flat = self.flatten(board)
        return ''.join(flat)

    def get_open_moves(self):
        """Return set of avaiable moves, given current state.

        State is string representation of flattened board.
        Action is position tuple of (row, col)
        """
        states = []
        actions = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == '-':
                    # Open position
                    action = (i, j)
                    actions.append(action)
                    # Make potential move and get board output
                    board = self.chomp(action, self.player)
                    state = self.get_state(board)
                    states.append(state)
        return states, actions

    def is_win(self):
        """Check win condition.

        Win means only the Poison block is left, and it is not your turn.
        There is no Draw.
        """
        for row in self.board:
            for val in row:
                if val == '-':
                    # Game not finished
                    return None
        # Only poison block left
        if self.player == 'X':
            return 'O'
        else:
            return 'X'

    def is_valid_move(self, action):
        """Validate action position tuple.

        Valid means in bounds and empty/not poison.
        """
        i = action[0]
        j = action[1]
        # Bounds check
        if (i < self.rows and i >= 0 and
                j < self.cols and j >= 0):
            # Empty/Poison check
            return self.board[i][j] == '-'
        else:
            return False

    def make_move(self, action):
        """Make move and toggle player."""
        # Make move
        self.board = self.chomp(action, self.player)
        # Toggle player
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'
        # Check win condition
        return self.is_win()

    def read_input(self):
        """Define game specific read in function from command line."""
        action = sys.stdin.readline().split(',')
        action[0] = int(action[0])
        action[1] = int(action[1])
        return action

    def print_board(self):
        for row in self.board:
            print(row)
        print('===============')

    def print_instructions(self):
        print('===============\n'
              'How to play:\n'
              'Possible moves are tuples of i,j where i is row # and j is col #\n'
              'Positions on the board:\n\n'
              '0,0 |  ...  | 0,N-1\n'
              '.\n'
              '.\n'
              '.\n'
              'M-1,0 | ... | M-1,N-1\n')
