""" Contains the connect4 board class """

import numpy as np


class Board():
    state = None

    def __init__(self, rows, columns, streak):
        """ Initializes the empty array """
        self.rows = rows
        self.columns = columns
        self.streak = streak
        self.state = np.zeros((self.rows, self.columns))
        self.current_player = None
        self.players = []

    def possible_moves(self):
        """ Returns the legal moves available moves """
        return [col for col in range(self.columns) if self.is_valid_move(col)]

    def place_piece(self, column: int):
        """ Adds the player's peice """
        occupancy = list(self.state[:, column] == 0)
        first_open = occupancy.index(True)
        self.state[first_open, column] = self.current_player.number
        self.current_player = self.current_player.opponent
        return self

    def is_valid_move(self, column) -> bool:
        """ Returns true if a player can drop a piece into the given column """
        if self.state[self.rows-1, column] != 0:
            return False

        return True

    def is_winning_board(self, player) -> bool:
        """ Returns true if the board is in a winning state for the given player """
        return any([
            self.check_vertical(player),
            self.check_horizontal(player),
            self.check_pos_diagonal(player),
            self.check_neg_diagonal(player)
        ])

    def check_vertical(self, player) -> bool:
        """ Checks for a vertical win """
        for col in range(self.columns):
            for row in range(self.rows-self.streak+1):
                if all(self.state[row:row+self.streak, col] == player.number):
                    return True

    def check_horizontal(self, player) -> bool:
        """ Checks for a vertical win """
        for row in range(self.rows):
            for col in range(self.columns-self.streak+1):
                if all(self.state[row, col:col+self.streak] == player.number):
                    return True

    def check_pos_diagonal(self, player) -> bool:
        for row in range(self.rows-self.streak+1):
            for col in range(self.columns-self.streak+1):
                if all([self.state[row+i, col+i] == player.number for i in range(self.streak)]):
                    return True

    def check_neg_diagonal(self, player) -> bool:
        board = np.flipud(np.copy(self.state))
        for row in range(self.rows-self.streak+1):
            for col in range(self.columns-self.streak+1):
                if all([board[row+i, col+i] == player.number for i in range(self.streak)]):
                    return True

    def print_board(self) -> None:
        """ Prints a pretty board """
        print(np.flipud(self.state))
