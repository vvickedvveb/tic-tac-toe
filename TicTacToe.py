# !/usr/bin/python

import sys
from TheMessages import TheMessages

class TicTacToe:
    def __init__(self, TheMessages):
        self.TheMessages = TheMessages()

    __board_dict = { # The board
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

    __WINNING_COMBO = [ # Winning combinations
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

    __XO = { # Standard 2 player symbols
        'EX': 'X',
        'OH': 'O'
    }

    player_turn = None # Who's playing
    win_row_count = 0 # need 3 to win
    ttl_move_count = 0 # Total moves
    played_pos = [] # Positions filled
    winner = False # True once 3 in row

    def the_board(self, ):
        """ Print out the board. """
        def __the_board_xo(board_pos):
            return '| ' + self.__ret_color(board_pos) + str(board_pos) + '\033[0m' + ' |'
        pr_board = ''
        for ct, board_pos in enumerate(self.__board_dict.values(), start=1): pr_board += __the_board_xo(board_pos) + '\n' if ct % 3 == 0 else __the_board_xo(board_pos)
        return pr_board

    def start(self, ):
        """ Start the game by determining if 'X' or 'O' goes first. """
        if self.player_turn == None:
            #self.__clr_scrn(2)
            text_input = self.TheMessages.get_message(['clr_yellow_back', 'bright', 'underline', 'clr_magenta'], 'enter_xo')
            enter_x_o = input(text_input)
            enter_x_o = enter_x_o.upper()
            if enter_x_o == 'Q': # Exit the game
                return 'break'

            if enter_x_o not in self.__XO.values():
                print(self.TheMessages.get_message(['clr_red'], 'must_xo'))
                return 'continue'

            self.player_turn = enter_x_o.upper()
        return self.player_turn

    def move(self, ):
        """ Enter & add position to place 'x'/'o' on board. """
        if self.ttl_move_count == 8 and not self.winner: # Last move, we'll play
            enter_pos = self.__last_move()
        else:
            try:
                enter_pos = input(f"""{self.TheMessages.get_message(['clr_magenta'], 'enter_pos')} '{self.player_turn}' """)
            except KeyboardInterrupt:
                print(f"\n\n{self.TheMessages.get_message(['clr_blue', 'clr_red_back'], 'quit_game')} '{self.player_turn}'\n\n")
                sys.exit(0)

            # Enter only positions on board
            if enter_pos not in self.__board_dict.keys():
                #self.__clr_scrn(1)
                print(self.TheMessages.get_message(['clr_cyan'], 'again_pos'))
                return 'continue'

            if enter_pos in self.played_pos:
                print(f"{self.TheMessages.get_message(['clr_red'], 'position')} {enter_pos} {self.TheMessages.get_message(['clr_red'], 'played')}")
                return 'continue'

        # Register position
        self.__board_dict[enter_pos] = self.player_turn
        self.played_pos.append(enter_pos)
        self.ttl_move_count += 1
        return True

    def determine_win(self, ):
        """ Determine 3 in a row for win. """
        for combo in self.__WINNING_COMBO:
            for el in combo:
                if self.__board_dict[el] == self.player_turn:
                    self.win_row_count += 1
            if self.win_row_count == 3:
                print(self.TheMessages.get_message(['clr_green'], 'winner') + self.player_turn.upper() + '\033[0m')
                self.winner = True
                print(self.the_board())
            self.win_row_count = 0
        return

    def turn(self, ):
        """ Switch turn's. """
        self.player_turn = self.__XO['OH'] if self.player_turn == self.__XO['EX'] else self.__XO['EX']
        return self.player_turn

    def reset_game(self, ):
        """ New game. Keep winning player starts. """
        self.win_row_count = 0
        self.ttl_move_count = 0
        self.played_pos = []
        self.winner = False
        self.__board_dict = {
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
        return True

    def main(self, ):
        """ All methods required for gameplay flow. void main() """
        while True:
            if self.winner:
                play_again = input(f"{self.TheMessages.get_message(['clr_blue'], 'play_again')}")
                if play_again.upper() == 'Y':
                    self.reset_game()
                    continue
                else:
                    break

            if self.ttl_move_count == 9 and not self.winner: # Last move, we'll pick
                print(f"{self.TheMessages.get_message(['red_back'], 'play_again')}")
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

            ttt.determine_win()

            if not self.winner:
                ttt.turn()
        return

    """                  """
    """ Méthodes Privées """
    """                  """
    def __clr_scrn(self, lines):
        """ Enter how many lines (int) to clear the screen. """
        # TODO: lambda switch
        if not type(lines) is int:
            lines = 5
        elif lines < 1:
            lines = 5
        elif lines > 15:
            lines = 100
        else:
            return [print('\n') for i in range(0, lines)]

    def __ret_color(self, board_pos):
        # TODO: put in another class
        if board_pos == 'X':
            the_color = '\033[33m'
        elif board_pos == 'O':
            the_color = '\033[36m'
        else:
            the_color = '\033[37m'
        return the_color


    def __last_move(self, ):
        """ Determine the last move """
        board_keys_set = set(self.__board_dict.keys())
        played_pos_set = set(self.played_pos)
        last_move = board_keys_set.difference(played_pos_set)
        last_move = next(iter(last_move))
        return str(last_move)


ttt = TicTacToe(TheMessages) # Start the game
if __name__ == '__main__':
    ttt.main()
