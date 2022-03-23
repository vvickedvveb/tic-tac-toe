class TheMessages:
    def __init__(self, ):
        pass

    __dict_colors = {
        # Colours
        'clr_red':        '\u001b[31m',
        'red_back':       '\u001b[41m',
        'clr_green':      '\u001b[32m',
        'green_back':     '\u001b[42m',
        'clr_blue':       '\u001b[34m',
        'clr_yellow':     '\u001b[33m',
        'clr_magenta':    '\u001b[35m',
        'clr_cyan':       '\u001b[36m',

        # Emphasis
        'bold':       '\u001b[1m',
        'underline':  '\u001b[4m',
        'background': '10',
        'bright':     ';1m',

        'end_color':  '\u001b[0m' # Call this at end of string else colour will continue.
    }

    __dict_messages = {
        'enter_xo': "Enter 'X' or 'O' to determine who goes first ('Q' to quit): ",
        'must_xo' : "You MUST enter either 'x' or 'o'!",
        'enter_pos': "Enter position [1 - 9] for player",
        'quit_game': "Game has unexpectedly ended by player",
        'again_pos': 'Please enter position [1 - 9]',
        'position': 'Position',
        'played': "already played",
        'winner': " WINNER is ",
        'play_again': "Play Again? ('Y'/'N'):"
    }
    # TODO: key error (not in list), slice


    def get_message(self, color, message):
        """ Return message with colour for game. """
        str_color = self.__get_color(color)
        return str_color + self.__dict_messages[message] + self.__dict_colors['end_color']


    def __get_color(self, list_color):
        """ Bold, underline, background etc... colours for messages. """

        print(self.__dict_colors['clr_red'])

        clr_len = len(list_color)
        the_clr = ''
        for count, clr in enumerate(list_color, start=1):
            the_clr += self.__dict_colors[clr]
        return the_clr

    def background_color(self):
        pass
