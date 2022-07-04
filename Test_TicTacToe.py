import unittest
import sys

def start(text_input):
    player_turn = None
    __XO = { # Standard 2 player symbols
        'EX': 'X',
        'OH': 'O'
    }

    if player_turn == None:
        enter_x_o = text_input
        enter_x_o = enter_x_o.upper()

        if enter_x_o == 'Q':
            return 'quit'

        if enter_x_o not in __XO.values():
            return False

        player_turn = enter_x_o.upper()

        return player_turn

"""
 move()
"""
def move_last(ttl_move_count, winner):
    if ttl_move_count == 8 and not winner:
        return 'last_move'

def move_in(enter_pos):
    __board_dict = {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }

    if enter_pos not in __board_dict.keys():
        print("Please enter position [1 - 9]")
        return enter_pos


def move(enter_pos, played_pos):
    __board_dict = {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }

    player_turn = 'X'
    ttl_move_count = 0

    if enter_pos in played_pos:
        print(f"Position {enter_pos} already played")
        return 'already_played'

    # Register position
    __board_dict[enter_pos] = player_turn
    played_pos.append(enter_pos)
    ttl_move_count += 1
    return True


def determine_win(player_turn, __board_dict, __WINNING_COMBO):
    win_row_count = 0
    winner = False
    for combo in __WINNING_COMBO:
        for x_or_o in combo:
            if __board_dict[x_or_o] == player_turn:
                win_row_count += 1
        if win_row_count == 3:
            print(f" WINNER IS {player_turn.upper()}")
            winner = True
        win_row_count = 0
    return winner


class TestTicTacToe(unittest.TestCase):
    def test_start_x_o(self):
        # Start: return X or O
        actual = start('o')
        expected = ['X', 'O']
        self.assertIn(actual, expected)


    def test_start_quit(self):
        # Start: Quit
        actual = start('q')
        expected = 'quit'
        self.assertEqual(actual, expected)


    def test_move_last(self):
        # Move: Last
        actual = move_last(8, False) # 8, False
        expected = 'last_move'
        self.assertEqual(actual, expected)


    def test_move_1_9(self):
        # Move: 1 - 9 only
        actual = move_in(9)
        expected = list(range(1, 10))
        self.assertIn(actual, expected)


    def test_move_played_pos(self):
        # Move: Played
        played_pos = [1, 3, 5, 7, 9]
        actual = move(3, played_pos)
        expected = 'already_played'
        self.assertEqual(actual, expected)

    def test_determine_win(self):
        __board_dict = {
            '1': 'x',
            '2': 'x',
            '3': 'x',
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9
        }
        __WINNING_COMBO = [
            # top pos. 1
            ('1', '2', '3'),
            ('1', '4', '7'),
            ('1', '5', '9'),
            # top pos. 2
            ('2', '5', '8'),
            # top pos. 3
            ('3', '5', '7'),
            ('3', '6', '9'),
            # mid. pos. 4
            ('4', '5', '6'),
            # bottom pos. 7
            ('7', '8', '9')
        ]
        player_turn = 'x'
        actual = determine_win(player_turn, __board_dict, __WINNING_COMBO)
        expected = True
        self.assertEqual(actual, expected)
