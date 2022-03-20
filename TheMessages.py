class TheMessages:
    def __init__(self, ):
        pass

    __dict_colors = {
        'red':        '\u001b[31m',
        'red_back':   '\u001b[41m',

        'green':      '\u001b[32m',
        'green_back': '\u001b[42m',

        'yellow':     '\u001b[33m',

        'magenta':    '\u001b[35m',
        'cyan':       '\u001b[36m',

        'Bold':       '\u001b[1m',
        'Underline':  '\u001b[4m',

        'bright':     ';1m', # Add brightness

        'end_color':  '\u001b[0m'
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

    def get_message(self, color, message):
        """ return the message to game. """
        return self.__dict_colors[color] + self.__dict_messages[message] + self.__dict_colors['end_color']
