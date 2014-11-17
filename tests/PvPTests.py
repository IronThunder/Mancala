__author__ = 'Duncan'

import unittest

from src.FunctionalPvP import *


class TestMancala(unittest.TestCase):

    def setUp(self):
        pass

    def test_opposite_pit(self):
        self.assertEqual(opposite_pit(3), 10)
        self.assertEqual(opposite_pit(5), 12)
        self.assertEqual(opposite_pit(11), 4)
        self.assertEqual(opposite_pit(13), 6)

    def test_distribute_normal_move(self):
        main_board = Board()
        main_board.pits = [0]*14
        main_board.pits[3] = 1
        (board, extra_turn) = main_board.distribute(3, 1)
        pits_to_test = get_pits(board)
        self.assertEqual(pits_to_test, [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertFalse(extra_turn)

    def test_distribute_past_khalana_move(self):
        main_board = Board()
        main_board.pits = [0]*14
        main_board.pits[12] = 2
        (board, extra_turn) = main_board.distribute(12, 2)
        pits_to_test = get_pits(board)
        self.assertEqual(pits_to_test, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
        self.assertFalse(extra_turn)
        main_board.pits = [0]*14
        main_board.pits[12] = 1
        (board, extra_turn) = main_board.distribute(12, 2)
        pits_to_test = get_pits(board)
        self.assertEqual(pits_to_test, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
        self.assertTrue(extra_turn)
        main_board.pits = [0]*14
        main_board.pits[11] = 3
        (board, extra_turn) = main_board.distribute(11, 2)
        pits_to_test = get_pits(board)
        self.assertEqual(pits_to_test, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2])
        self.assertFalse(extra_turn)

    def test_distribute_into_khalana_move(self):
        main_board = Board()
        main_board.pits = [0]*14
        main_board.pits[12] = 1
        (board, extra_turn) = main_board.distribute(12, 2)
        pits_to_test = get_pits(board)
        self.assertEqual(pits_to_test, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
        self.assertTrue(extra_turn)

    def test_board_layout(self):
        main_board = Board()
        main_board.pits = [0]*14
        self.assertEqual(text_board_layout(main_board), ('          Player 1', '      0  0  0  0  0  0', '0                               0', '      0  0  0  0  0  0', '          Player 2'))

    def test_test_player_move(self):
        player = TestPlayer()
        player.string = '5'
        self.assertEqual(player.move(None, None, None), '5')
        player.string = '12'
        self.assertEqual(player.move(None, None, None), '12')
        player.string = '3'
        self.assertEqual(player.move(None, None, None), '3')

    def test_check_input_validity(self):
        robot = TestPlayer()
        main_board = Board()
        main_board.pits = [0]*14
        main_board.pits[4] = 1
        self.assertFalse(check_input_validity('4', robot, main_board))
        self.assertTrue(check_input_validity('nope', robot, main_board))

    def test_winner(self):
        main_board = Board()
        main_board.pits = [0]*14
        (game_over, player, score) = check_winner(main_board)
        self.assertTrue(game_over)
        self.assertEqual(player, 0)
        self.assertEqual(score, 0)
        main_board.pits = [0]*14
        main_board.pits[3] = 1
        (game_over, player, score) = check_winner(main_board)
        self.assertTrue(game_over)
        self.assertEqual(player, 1)
        self.assertEqual(score, 1)
        main_board.pits = [0]*14
        main_board.pits[8] = 2
        (game_over, player, score) = check_winner(main_board)
        self.assertTrue(game_over)
        self.assertEqual(player, 2)
        self.assertEqual(score, 2)
        main_board.pits = [0]*14
        main_board.pits[8] = 2
        main_board.pits[3] = 2
        (game_over, player, score) = check_winner(main_board)
        self.assertFalse(game_over)

if __name__ == '__main__':
    unittest.main()