class TicTacToe(object):
    """
    Tic Tac Toe is the game class that handles win conditions,
    board state updates, and checks validity of moves
    """

    def __init__(self):
        """
        Construct new tictactoe game instance
        """
        self.board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        self.player = 'X'
        self.winner = None

    def reset(self):
        self.board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        self.player = 'X'
        self.winner = None

    def available_moves(self):
        """
        Generates list of available moves given current state and associated next states
        """
        actions = []
        states = []
        for i, val in enumerate(self.board):
            if val == '-':
                actions.append(i)
                self.board[i] = self.player
                states.append(self.get_state(self.board))
                self.board[i] = '-'
        return states, actions

    def get_state(self, board):
        """
        Generates board state as String
        """
        return ''.join(board)

    def check_win_condition(self):
        """
        Check the board to see if there is a possible winner or terminal condition (cat)
        """
        state = self.get_state(self.board)
        # Check win condition
        row_1 = state[:3]
        row_2 = state[3:6]
        row_3 = state[6:]
        col_1 = state[0] + state[3] + state[6]
        col_2 = state[1] + state[4] + state[7]
        col_3 = state[2] + state[5] + state[8]
        diag_1 = state[0] + state[4] + state[8]
        diag_2 = state[2] + state[4] + state[6]
        triples = [row_1, row_2, row_3, col_1, col_2, col_3, diag_1, diag_2]

        for triple in triples:
            if (triple == 'OOO'):
                return 'O'
            elif (triple == 'XXX'):
                return 'X'

        # Check draw condition
        if '-' not in self.board:
            return 'Draw'

        return None

    def is_valid_move(self, position):
        """
        Check that potential move is in a valid position
        Valid meaning inbounds and not occupied
        """
        if position >= 0 and position < len(self.board):
            return self.board[position] == '-'
        else:
            return False

    def make_move(self, position):
        """
        Makes move by setting position to player value and toggles player
        Returns check_win_condition result
        """
        self.board[position] = self.player
        self.player = 'O' if self.player == 'X' else 'X'
        return self.check_win_condition()

    def print_board(self):
        print '{} {} {}\n{} {} {}\n{} {} {}'.format(self.board[0], self.board[1], self.board[2],
                                                    self.board[3], self.board[4], self.board[5],
                                                    self.board[6], self.board[7], self.board[8])
        print '====='
