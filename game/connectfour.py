"""Connect Four."""


from game import Game


class ConnectFour(Game):
    """Connect Four game class."""

    def __init__(self, rows=6, cols=7):
        """Construct new Connect Four game instance.

        The most commonly used Connect Four board size is 7 columns x 6 rows.
        Size variations include 8x7, 9x7, 10x7, 8x8
        """
        self.rows = rows
        self.cols = cols
        self.board = self.create_board(rows, cols)
        self.player = 'X'
        self.winner = None

    def create_board(self, rows, cols):
        """Create empty board of size rows x cols."""
        board = []
        for i in range(rows * cols):
            board.append('-')
        return board

    def reset(self):
        """Reset board between games."""
        self.board = self.create_board(self.rows, self.cols)
        self.player = 'X'
        self.winner = None

    def get_open_moves(self):
        """Returns list of available moves given current states and next states."""
        actions = []
        states = []

        for i in range(self.cols):
            column_indices = self.get_column_indices(i)
            column_indices.reverse()
            for j in column_indices:
                # Iterate over input column backwards (bottom up) to determine drop landing position
                if self.board[j] == '-':
                    # Find first empty spot from bottom and 'drop' token there
                    self.board[j] = self.player
                    states.append(self.get_state(self.board))
                    # Record column num as action
                    actions.append(i)
                    self.board[j] = '-'
                    break
        return states, actions

    def get_state(self, board):
        """Returns board state as String."""
        return ''.join(board)

    def get_grid(self, board):
        """Returns grid 2D representation of board."""
        grid = []
        for i in range(self.rows):
            grid.append([])
            for j in range(self.cols):
                grid[i].append(board[(i * self.cols) + j])
        return grid

    def get_column_indices(self, col):
        """Return column indices of board at column position."""
        column_indices = []
        # Find index of bottom position in selected column
        bottom = len(self.board) - (self.cols - col)
        for i in range(col, bottom + 1, self.cols):
            column_indices.append(i)
        return column_indices

    def is_win(self):
        """Check the board for win condition.

        Possible outputs are X, O, Draw, None.
        """
        # Convert to 2D array for ease of implementaiton
        grid = self.get_grid(self.board)

        # Check horizontal, vertical, and diagonal sequences for four in a row
        for i in range(self.rows):
            for j in range(self.cols):
                if j <= self.cols - 4:
                    # Horizontal
                    sequence = grid[i][j] + grid[i][j + 1] + grid[i][j + 2] + grid[i][j + 3]
                    if sequence == 'XXXX':
                        return 'X'
                    elif sequence == 'OOOO':
                        return 'O'
                if i <= self.rows - 4:
                    # Vertical
                    sequence = grid[i][j] + grid[i + 1][j] + grid[i + 2][j] + grid[i + 3][j]
                    if sequence == 'XXXX':
                        return 'X'
                    elif sequence == 'OOOO':
                        return 'O'
                if i <= self.rows - 4 and j <= self.cols - 4:
                    # Diagonal Right
                    sequence = grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] + grid[i + 3][j + 3]
                    if sequence == 'XXXX':
                        return 'X'
                    elif sequence == 'OOOO':
                        return 'O'
                if i <= self.rows - 4 and j >= 3:
                    # Diagonal Left
                    sequence = grid[i][j] + grid[i + 1][j - 1] + grid[i + 2][j - 2] + grid[i + 3][j - 3]
                    if sequence == 'XXXX':
                        return 'X'
                    elif sequence == 'OOOO':
                        return 'O'
        # Check Draw condition
        if '-' not in self.board:
            return 'Draw'

        # Unfinished game
        return None

    def is_valid_move(self, col):
        """Check that potential column selection is valid.

        Valid means inbounds and column is not completely occupied.
        """
        if col >= 0 and col < self.cols:
            column_indices = self.get_column_indices(col)
            for i in column_indices:
                if self.board[i] == '-':
                    return True
            return False
        else:
            return False

    def make_move(self, col):
        """Makes move by vertically dropping token in column #col.

        Also toggles player and returns is_win result.
        """
        # Find index of bottom position in selected column
        column_indices = self.get_column_indices(col)
        column_indices.reverse()
        for i in column_indices:
            # Iterate over input column backwards (bottom up) to determine drop landing position
            if self.board[i] == '-':
                # Find first empty spot from bottom and 'drop' token there
                self.board[i] = self.player
                break
        self.player = 'O' if self.player == 'X' else 'X'
        return self.is_win()

    def print_board(self):
        s = ''
        for i in range(self.rows * self.cols):
            s += self.board[i] + ' '
            if ((i + 1) % self.cols == 0 and
                    (i + 1) < self.rows * self.cols):
                s += '\n'
        print(s)
        print('===============')

    def print_instructions(self):
        print('===============\n'
              'How to play:\n'
              'Possible moves are [0,N) where N is cols\n'
              'Selecting a column drops a piece vertically in that column\n\n'
              'Corresponding to these spaces on the board:\n\n'
              '0 | 1 | 2 | ... | N - 1\n'
              '.\n'
              '.\n'
              '.\n'
              '. | . | . | ... | . \n')
