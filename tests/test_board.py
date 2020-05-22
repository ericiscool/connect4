from connect_four.board import Board


def test_board():
    my_board = Board(rows=6, columns=7, streak=4)
    assert my_board.rows == 6
