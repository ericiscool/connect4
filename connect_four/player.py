"""
Contains all of the connect4 players agents
"""

import copy
import random


class GenericPlayer():
    """ The generic type that all agents must extend """

    def __init__(self, name: str, number: int, game):
        self.name = name
        self.number = number
        self.opponent = None
        self.game = game

    def get_move(self, board):
        """ Given the board, return the players move as a column index """
        pass


class RandomPlayer(GenericPlayer):
    """ agent that chooses random move """

    def get_move(self, board):
        while True:
            proposed_column = random.choice(range(self.game.columns))
            if board.is_valid_move(proposed_column):
                print(f"{self.name} is playing at column {proposed_column}")
                return proposed_column


class BetterRandomPlayer(GenericPlayer):
    """ agent that chooses random move """

    def get_move(self, board):
        for col in board.possible_moves():
            board_copy = copy.deepcopy(board)
            if board_copy.place_piece(col).is_winning_board(self.opponent):
                print(f"{self.name} is playing at column {col}")
                return col
        while True:
            proposed_column = random.choice(range(self.game.columns))
            if board.is_valid_move(proposed_column):
                print(f"{self.name} is playing at column {proposed_column}")
                return proposed_column


class CommandLinePlayer(GenericPlayer):
    """ Users that are playing through the command line """

    def get_move(self, board):
        board.print_board()

        # repeatedly ask for input until the user returns valid input
        while True:
            proposed_column = input("{self.name:}, which column would you like to play in?")
            try:
                proposed_column = int(proposed_column)
                if board.is_valid_move(proposed_column):
                    return proposed_column
            except:
                print("dummy")
                print("If you're not gonna play right don't play at all!")

            else:
                print("Please choose a valid move.")


class MinMaxPlayer(GenericPlayer):
    """ An AI player that uses minmax to choose places """
    def get_move(self, board):
        pass

    def evaluate_value(self, board):
        pass

    def calc_max(self, board):
        pass

    def board_min(self, board):
        pass
