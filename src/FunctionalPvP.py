from ConsoleUI import *
from GraphicUI import *

UIManager = GraphicUI()
UIManager.initialize()


class HumanPlayer:
    def __init__(self):
        self.number = 1


class Board:
    def __init__(self):
        self.pits = []

    def distribute(self, pit_num, player):
        extra_turn = False
        new_board = Board()
        new_board.pits = self.pits
        value = new_board.pits[pit_num]
        new_board.pits[pit_num] = 0
        current_pit = pit_num
        for i in range(value):
            if current_pit >= 13:
                current_pit = -1
            current_pit += 1
            new_board.pits[current_pit] += 1
        if current_pit != 6 and current_pit != 13:
            if new_board.pits[current_pit] == 1 and player == 1:
                new_board.pits[6] += new_board.pits[opposite_pit(current_pit)]
                new_board.pits[opposite_pit(current_pit)] = 0
            elif new_board.pits[current_pit] == 1 and player == 2:
                new_board.pits[13] += new_board.pits[opposite_pit(current_pit)]
                new_board.pits[opposite_pit(current_pit)] = 0
        if current_pit == 6 and player == 1 or current_pit == 13 and player == 2:
            extra_turn = True
        return new_board, extra_turn


def opposite_pit(pit):
    if pit != 6 and pit != 13:
        return 12 - pit
    raise ValueError


def get_pits(board):
    pits = board.pits
    return pits


def check_input_validity(user_input, player, board):
    if not user_input.isdigit():
        return True
    entered_pit = int(user_input)
    if entered_pit > 5 and player.number == 1:
        return True
    if entered_pit < 7 and player.number == 2:
        return True
    if entered_pit > 12:
        return True
    if board.pits[entered_pit] == 0:
        return True


def check_winner(board):
    pits = get_pits(board)
    player1_score = 0
    player2_score = 0
    player1_board = False
    player2_board = False
    for i in range(6):
        player1_score += pits[i]
        if pits[i] != 0:
            player1_board = True
    for i in range(7, 13):
        player2_score += pits[i]
        if pits[i] != 0:
            player2_board = True
    player1_score += pits[6]
    player2_score += pits[13]
    if player1_board and player2_board:
        return False, None, None
    elif player1_score > player2_score:
        return True, 1, player1_score
    elif player2_score > player1_score:
        return True, 2, player2_score
    elif player1_score == player2_score:
        return True, 0, player1_score


def play_game():
    board = Board()
    board.pits = [3]*14
    board.pits[6] = 0
    board.pits[13] = 0
    winner = 4
    player1 = HumanPlayer()
    player2 = HumanPlayer()
    player1.number = 1
    player2.number = 2
    players = [player1, player2]
    current_player = 1
    extra_turn = False
    invalid = False
    while winner == 4:
        selected_move = UIManager.move(extra_turn, invalid, current_player, board)
        if check_input_validity(selected_move, players[current_player-1], board):
            invalid = True
            continue
        invalid = False
        (new_board, check_extra_turn) = board.distribute(int(selected_move), current_player)
        extra_turn = check_extra_turn
        board = new_board
        (game_over, victor, score) = check_winner(new_board)
        if game_over:
            winner = victor
            UIManager.display_winner(winner, score)
        if not extra_turn:
            if current_player == 1:
                current_player = 2
            else:
                current_player = 1
    while 1:
        pass


if __name__ == "__main__":
    print play_game()