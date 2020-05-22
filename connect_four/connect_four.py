from itertools import cycle
from .board import Board
from .player import CommandLinePlayer, BetterRandomPlayer

ROWS = 6
COLUMNS = 7
STREAK = 4


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

    def add_player(self, player):
        self.players.append(player)

    def set_opponents(self):
        self.players[0].opponent = self.players[1]
        self.players[1].opponent = self.players[0]


def main_loop(game):

    player_gen = cycle(game.players)

    game_over = False
    # Play the loop
    while not game_over:
        current_player = next(player_gen)
        move = current_player.get_move(game.board)
        game.board.place_piece(move, current_player)

        # Print congrats if the game is over
        if game.board.is_winning_board(current_player):
            game.board.print_board()
            print("Yayyyy")
            game_over = True


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Play connect 4')
    parser.add_argument('--simulate', help='Game is run between two computer agents', action="store_true")
    args = parser.parse_args()

    # Initialize the Game
    game = Game(ROWS, COLUMNS, STREAK)

    # Setup players
    if args.simulate:
        game.add_player(BetterRandomPlayer('Player 2', 1, game))
        game.add_player(BetterRandomPlayer('Player 2', 2, game))

    else:
        game.add_player(CommandLinePlayer('Player 1', 1, game))
        game.add_player(BetterRandomPlayer('Player 2', 2, game))

    game.set_opponents()

    main_loop(game)
