# !/usr/bin/python


# Play Again
# Enter either x or o --------------------- DONE
# Enter pos ONLY -------------------------- DONE
# Check empty ----------------------------- DONE
# Check if picked already ----------------- DONE
# Show chosen in message ------------------ DONE
# add color to x/o ------------------------ DONE
# Case ------------------------------------ DONE
# NO Winner ------------------------------- DONE
# Predict last move ----------------------- DONE
# Board should loop ----------------------- DONE
# Enhance visual
# Put messages in dict
# Time between moves
# Total time to play
# camelCase or "sn_a_ke" ------------------ DONE
# make x/o a dict
# Colors class https://pkg.go.dev/github.com/whitedevops/colors#section-readme
# Ctrl + C to quit

# Demonstrate a comprehension / 1 liner --- DONE
# Demonstrate a lambda
# Demonstrate classes --------------------- DONE
# Improve class, private, dataclass inherit ...
# Demonstrate a ternary ------------------- DONE
# Demonstrate itertools -----------
# Demonstrate Try
# Comments

# TEST
# self play
# test wins

# Play Computer

# Is there better way to write this?

class TicTacToe:
    board_dict = { # The board
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

    winning_combo = [ # Winning combinations
        # top pos. 1
        ['1', '2', '3'],
        ['1', '4', '7'],
        ['1', '5', '9'],
        # top pos. 2
        ['2', '5', '8'],
        # top pos. 3
        ['3', '5', '7'],
        ['3', '6', '9'],
        # mid. pos. 4
        ['4', '5', '6'],
        # bottom pos. 7
        ['7', '8', '9']
    ]

    player_x = []
    player_o = []
    # make this a dict
    player_XO = {
        'playerX': None,
        'playerY': None,
    }

    player_turn = None
    win_row_count = 0 # need 3 to win
    ttl_move_count = 0 # Total moves
    played_pos = [] # Positions filled
    winner = False
    board_pos = ''

    # TODO: args kwargs?
    def __init__(self, ):
        pass

    def __ret_color(self, board_pos):
        # TODO: determine if ok?
        if board_pos == 'X':
            the_color = '\033[33m'
        elif board_pos == 'O':
            the_color = '\033[36m'
        else:
            the_color = '\033[37m'
        return the_color

    def the_board(self, ):
        def __the_board_xo(board_pos):
            return '| ' + self.__ret_color(board_pos) + str(board_pos) + '\033[0m' + ' |'

        """ Print out the board. """
        pr_board = ''
        the_board_xo = ''

        for ct, board_pos in enumerate(self.board_dict.values(), start=1): pr_board += __the_board_xo(board_pos) + '\n' if ct % 3 == 0 else __the_board_xo(board_pos)

        return pr_board

    def start(self, ):
        if self.player_turn == None:
            input_text = "Enter 'X' or 'O' to determine who goes first ('Q' to quit): "
            enter_x_o = input(input_text)
            enter_x_o = enter_x_o.upper()

            # Exit the game
            if enter_x_o == 'Q':
                return 'break'

            if enter_x_o not in ['X', 'O']:
                print("You MUST enter Either 'x' or 'o'!")
                return 'continue'

            self.player_turn = enter_x_o.upper()

        return self.player_turn

    def move(self):
        def __last_move(self, ):
            """ Determine the last move """
            board_keys_set = set(self.board_dict.keys())
            played_pos_set = set(self.played_pos)
            last_move = board_keys_set.difference(played_pos_set)
            last_move = next(iter(last_move))
            return str(last_move)


        if self.player_turn.upper() == 'X':
            input_text = "for player 'X': "
        else:
            input_text = "for player 'O': "

        if self.ttl_move_count == 8 and not self.winner: # Last move
            enter_pos =__last_move()
        else:
            enter_pos = input(f"""Enter position [1 - 9] {input_text}""")

            # Enter only positions on board
            print(type(self.board_dict.keys()))
            print('enter_pos: ', enter_pos)
            if enter_pos not in self.board_dict.keys():
                print('\033[93m' + 'Please enter position' + '\033[0m')
                return 'continue'

            if enter_pos in self.played_pos:
                print(f'Postion {enter_pos} already played')
                return 'continue'

        # Register position
        self.board_dict[enter_pos] = self.player_turn
        self.played_pos.append(enter_pos)
        self.ttl_move_count+=1

        return True

    def determine_win(self, ):
        for combo in self.winning_combo:
            for el in combo:
                if self.board_dict[el] == self.player_turn: # 'X' or 'O'
                    self.win_row_count += 1
            if self.win_row_count == 3:
                print('\033[92m' + "WINNER is " + self.player_turn.upper() + '\033[0m')
                self.winner = True
            self.win_row_count = 0

    def turn(self):
        """ Switch user turn """
        self.player_turn = 'O' if self.player_turn == 'X' else 'X'

    def main(self):
        """ void main() """
        while True:
            if self.winner:
                play_again = input("Play Again? ('Y'/'N'): ")
                if play_again.upper() == 'Y':
                    # TODO: make a func, keep player turn
                    #player_turn = None
                    self.win_row_count = 0
                    self.ttl_move_count = 0
                    self.played_pos = []
                    self.winner = False
                    self.board_pos = ''
                    self.board_dict = {
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
                    continue
                else:
                    break

            the_board = ttt.the_board()
            print(the_board)

            br_con = ttt.start()
            if br_con == 'break':
                break
            if br_con == 'continue':
                continue

            br_con = ttt.move()
            if br_con == 'continue':
                continue

            br_con = ttt.determine_win()
            if br_con == 'break':
                break

            if not self.winner:
                ttt.turn()

    """ def repr(self):
        return f"{}" """


# Game play
ttt = TicTacToe()

if __name__ == '__main__':
    ttt.main()
