""" Connect Four
The primary game controller
"""

import tkinter as tk
from itertools import cycle
from .board import Board
from .player import CommandLinePlayer, BetterRandomPlayer
from .GameTree import GameTree, GameNode

ROWS = 3
COLUMNS = 4
STREAK = 3


class Game():
    """
    The game controler.
    Contains game parameters, the board, and the players.
    """

    def __init__(self, rows, columns, streak):
        self.board = Board(ROWS, COLUMNS, STREAK)
        self.players = []
        self.rows = rows
        self.columns = columns
        self.streak = streak
        print(f"Creating game with {rows} rows and {columns} columns")

    def add_player(self, player):
        """ Adds the given player to the game's list of players """
        self.players.append(player)
        self.board.players.append(player)

    def set_opponents(self):
        self.players[0].opponent = self.players[1]
        self.players[1].opponent = self.players[0]


def main_loop(game):
    " Iterates over players until game is over """
    player_gen = cycle(game.players)

    game_over = False
    # Play the loop
    while not game_over:
        current_player = next(player_gen)
        game.board.current_player = current_player

        # Build the tree
        root = GameNode(game.board)
        gt = GameTree(root=root)
        gt.build_tree()

        move = current_player.get_move(game.board)
        game.board.place_piece(move)

        # Print congrats if the game is over
        if game.board.is_winning_board(current_player):
            game.board.print_board()
            print("Yayyyy")
            game_over = True


class GameWindow(tk.Frame):
    """ The pyglet window that displays the game
    """
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.pack()
        # self.init_board()



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Play connect 4')
    parser.add_argument('--simulate', help='Game is run between two computer agents', action="store_true")
    args = parser.parse_args()

    # Initialize the Game
    game = Game(ROWS, COLUMNS, STREAK)

    # Setup players
    if args.simulate:
        game.add_player(BetterRandomPlayer('Player 1', 1, game))
        game.add_player(BetterRandomPlayer('Player 2', 2, game))

    else:
        game.add_player(CommandLinePlayer('Player 1', 1, game))
        game.add_player(BetterRandomPlayer('Player 2', 2, game))

    game.set_opponents()


    main_loop(game)


