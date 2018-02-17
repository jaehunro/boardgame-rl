"""Abstract base class for board games."""


from abc import ABCMeta, abstractmethod


class Game(object):
    """General Game Abstract base class."""

    __metaclass__ = ABCMeta

    @abstractmethod
    def get_open_moves(self):
        """Retrieve next move options."""
        raise NotImplementedError('Get open moves must be implemented.')

    @abstractmethod
    def get_state(self):
        """Retrieve game state."""
        raise NotImplementedError('Get game state must be implemented.')

    @abstractmethod
    def is_win(self):
        """Check win condition."""
        raise NotImplementedError('Win condition check must be implemented.')

    @abstractmethod
    def is_valid_move(self):
        """Validate move."""
        raise NotImplementedError('Move validation must be implemented.')

    @abstractmethod
    def make_move(self):
        """Make move."""
        raise NotImplementedError('Make move must be implemented.')

    @abstractmethod
    def print_board(self):
        """Print game board."""
        raise NotImplementedError('Print board must be implemented.')
        
    @abstractmethod
    def read_input(self):
        """Read input from command line."""
        raise NotImplementedError('Read input must be implemented.')

    @abstractmethod
    def reset(self):
        """Reset board game."""
        raise NotImplementedError('Reset must be implemented.')
