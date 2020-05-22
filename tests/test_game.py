from connect_four.connect_four import Game, main_loop
from connect_four.player import BetterRandomPlayer


def test_game():
    """ Tests to make sure the game can run """
    # Initialize the Game
    game = Game(6, 7, 4)

    game.add_player(BetterRandomPlayer('Player 2', 1, game))
    game.add_player(BetterRandomPlayer('Player 2', 2, game))

    game.set_opponents()
    main_loop(game)
