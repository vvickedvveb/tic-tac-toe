from pprint import pprint


class TheMessages:
    def __init__(self, ):
        pass

    __dict_colors = {
        # Colours
        'clr_red':        '\u001b[31m',
        'clr_green':      '\u001b[32m',
        'clr_blue':       '\u001b[34m',
        'clr_yellow':     '\u001b[33m',
        'clr_magenta':    '\u001b[35m',
        'clr_cyan':       '\u001b[36m',

        # Emphasis
        'bold':           '\u001b[1m',
        'underline':      '\u001b[4m',
        'background':     '10', # Add this value to the colour to make it a background colour.
        'bright':         ';1m',

        'end_color':  '\u001b[0m' # Call at end of string else colour will bleed.
    }

    __dict_messages = {
        'enter_xo': "Enter 'X' or 'O' to determine who goes first ('Q' to quit):",
        'must_xo' : "You MUST enter either 'x' or 'o'!",
        'enter_pos': "Enter position [1 - 9] for player",
        'quit_game': "Game has unexpectedly ended by player",
        'again_pos': 'Please enter position [1 - 9]',
        'position': 'Position',
        'played': "already played",
        'winner': " WINNER is ",
        'play_again': "Play Again? ('Y'/'N'):"
    }


    def get_message(self, list_color, message):
        #TODO: keyerror
        """ Get message for input and to display for game.
            Args: list_color (string): List of colours and/or emphasis.
                  message (string): The text to be displayed.
            Returns: string: Text with concatenated colour. """
        str_color = self.__get_color(list_color)
        return str_color + self.__dict_messages[message] + self.__dict_colors['end_color']


    def __get_color(self, list_color):
        """ Bold, underline, background etc... colours for messages. """
        #TODO: default color, keyerror
        the_clr = ''

        def __background_color(clr):
            """ Background colour. """
            bg_color = ''
            bg_color += self.__dict_colors[clr[:-5]][0:2]
            temp_bg_color = int(self.__dict_colors[clr[:-5]][2:-1]) + int(self.__dict_colors['background'])
            bg_color += str(temp_bg_color)
            bg_color += self.__dict_colors[clr[:-5]][-1]
            return bg_color

        def __emph_font(clr):
            """ Add emphasis to non-background colour. """
            font_clr = ''
            emph_font = ''
            font_clr = self.__dict_colors[clr]

            if 'bold' in list_color:
                emph_font += self.__dict_colors['bold']

            if 'underline' in list_color:
                emph_font += self.__dict_colors['underline']

            if 'bright' in list_color:
                font_clr = font_clr[:-1]
                font_clr += self.__dict_colors['bright'] # add after font colour

            return emph_font + font_clr

        for clr in list_color:
            if clr[-5:] == '_back': # background colour
                the_clr += __background_color(clr)
            elif clr[0:3] == 'clr' and not clr[-5:] == '_back': # emphasize the font colour
                the_clr += __emph_font(clr)
        pprint(the_clr)
        return the_clr
