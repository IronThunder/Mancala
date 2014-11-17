__author__ = 'Duncan'
import sys


def text_board_layout(board):
    pits = board.pits
    return ('          Player 1',
            '      %d  %d  %d  %d  %d  %d' % (pits[0], pits[1], pits[2], pits[3], pits[4], pits[5]),
            '%d                               %d' % (pits[13], pits[6]),
            '      %d  %d  %d  %d  %d  %d' % (pits[12], pits[11], pits[10], pits[9], pits[8], pits[7]),
            '          Player 2')


class ConsoleUI:
    def __init__(self):
        pass

    def initialize(self):
        pass

    def draw_board(self, board):
        print("\n".join(text_board_layout(board)))

    def move(self, extra_turn, invalid, number, board):
        self.draw_board(board)
        if not extra_turn and not invalid:
            print 'Player %d, enter the pit you would like to move from.' % number
        elif extra_turn and not invalid:
            print 'You ended in your Khalana. Take an extra turn. Enter another pit'
        elif invalid:
            print 'Invalid move. Please enter the number of a pit that stones in it that is on your side.'
        else:
            raise Exception('next_turn method failure')
        input = raw_input()
        return input

    def display_winner(self, victor, score):
        if victor == 0:
            print "The game ends in a tie. Congratulations. The odds of this happening are very slim."
        elif victor == 1:
            print "The game ends with a victory for player 1! The final score was %d to %d." % (score, 36-score)
        elif victor == 2:
            print "The game ends with a victory for player 2! The final score was %d to %d." % (score, 36-score)
        sys.exit()