# Play Again
# Enter either x or o --------------------- DONE
# Enter pos ONLY -------------------------- DONE
# Check empty ----------------------------- DONE
# Check if picked already ----------------- DONE
# Show chosen in message
# add color to x/o ------------------------ DONE
# Case ------------------------------------ DONE (FOR POS)
# NO Winner ------------------------------- DONE
# Predict last move ----------------------- DONE
# Board should loop ----------------------- DONE
# Enhance visual
# Put messages in dict
# Time between moves
# Total time to play
# camelCase or sn_a_ke -------------------- DONE
# make x/o a dict
# Tests
# Put colors in class https://pkg.go.dev/github.com/whitedevops/colors#section-readme

# Demonstrate a comprehension / 1 liner --- DONE
# Demonstrate a lambda
# Demonstrate classes --------------------- DONE
# Improve class, private, dataclass etc...
# Demonstrate a ternary ------------------- DONE
# Demonstrate itertools -----------
# Demonstrate Try

# Is there better way to write this?

import enum


class TicTacToe:
    board_dict = { # The board
        'tl': 1,
        'tm': 2,
        'tr': 3,
        'ml': 4,
        'mm': 5,
        'mr': 6,
        'bl': 7,
        'bm': 8,
        'br': 9
    }

    winning_combo = [ # Winning combinations
        # tl - 1
        ['tl', 'tm', 'tr'],
        ['tl', 'ml', 'bl'],
        ['tl', 'mm', 'br'],
        # tm, mm - 2
        ['tm', 'mm', 'bm'],
        # tr - 3
        ['tr', 'mm', 'bl'],
        ['tr', 'mr', 'br'],
        # ml - 4
        ['ml', 'mm', 'mr'],
        # mm == tm
        # mr == tr & ml
        # bl
        ['bl', 'bm', 'br']
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
    th_brd = ''
    board_pos = ''

    # TODO: args kwargs?
    def __init__(self,):
        pass

    def the_board(self):
        def _ret_color(board_pos):
            # TODO: determine if ok?
            if board_pos == 'X':
                the_color = '\033[33m'
            elif board_pos == 'O':
                the_color = '\033[36m'
            else:
                the_color = '\033[37m'

            return the_color


        """ Print out the board. """
        pr_board = ''
        the_board_xo = ''
        #the_color = ''
        """ for ct, board_pos in enumerate(self.board_dict.values(), start=1):
            pr_board += '| ' + _ret_color(board_pos, ) + str(board_pos) + '\033[0m' + ' |'
            # TODO: exception
            if ct % 3 == 0:
                pr_board += '\n' """

        def _the_board_xo(board_pos):
            return '| ' + _ret_color(board_pos, ) + str(board_pos) + '\033[0m' + ' |'

        for ct, board_pos in enumerate(self.board_dict.values(), start=1): pr_board += _the_board_xo(board_pos) + '\n' if ct % 3 == 0 else _the_board_xo(board_pos)

        #self.th_brd = ['| ' + _ret_color(self.board_pos ) + str(self.board_pos) + '\033[0m' + ' |' for ct, self.board_pos in enumerate(self.board_dict.values(), start=1)]

        return pr_board


    def start(self, ):
        if self.player_turn == None:
            input_text = "Enter 'X' or 'O' to determine who goes first ('Q' to quit): "
            enter_x_o = input(input_text)
            enter_x_o = enter_x_o.upper()

            if enter_x_o == 'Q':
                return 'break'

            if enter_x_o not in ['X', 'O']:
                print("You MUST enter Either 'x' or 'o'!")
                return 'continue'

            self.player_turn = enter_x_o.upper()

        return self.player_turn

    def move(self):
        if self.player_turn.upper() == 'X':
            input_text = "for player 'X': "
        else:
            input_text = "for player 'O': "

        # Make last move
        if self.ttl_move_count == 8 and not self.winner:
            # Compare
            # TODO: private
            board_keys_set = set(self.board_dict.keys())
            played_pos_set = set(self.played_pos)
            last_move = board_keys_set.difference(played_pos_set)
            last_move = next(iter(last_move))
            enter_pos = str(last_move)
        else:
            enter_pos = input(f"""Enter position
            (tl tm tr)
            (ml mm mr)
            (bl bm br) {input_text}""")

            # Enter only positions on board
            if enter_pos not in self.board_dict.keys():
                print('\033[93m' + 'Please enter position' + '\033[0m')
                return 'continue'

            if enter_pos in self.played_pos:
                print(f"Postion {enter_pos} already played")
                return 'continue'

        # Register position
        self.board_dict[enter_pos] = self.player_turn
        self.played_pos.append(enter_pos)
        self.ttl_move_count+=1

        return True

    def determine_win(self, ):
        for combo in self.winning_combo:
            #print("combo: ", combo)
            for el in combo:
                #print('el: ', board_dict[el], el)
                if self.board_dict[el] == self.player_turn: # 'X' or 'O'
                    self.win_row_count += 1
                    #print("board_dict[el]: ", el, board_dict[el], win_row_count)
                    #print("win_row_count: ", win_row_count)
                    #print(board_dict[el])
            if self.win_row_count == 3:
                print('\033[92m' + "WINNER is " + self.player_turn.upper() + '\033[0m')
                self.winner = True
                break
            self.win_row_count = 0

        if self.winner:
            return 'break'

    def turn(self):
        """ Switch user turn """
        self.player_turn = 'O' if self.player_turn == 'X' else 'X'

    def main(self):
        while True:
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

            ttt.turn()

    def repr(self):
        return f"{self.th_brd}"


# Game play
ttt = TicTacToe()

if __name__ == '__main__':
    ttt.main()
