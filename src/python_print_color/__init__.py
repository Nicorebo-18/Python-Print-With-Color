#########################################################################################################
#                                                                                                       #
#         _____       _   _                   _____      _       _      _____      _                    #
#        |  __ \     | | | |                 |  __ \    (_)     | |    / ____|    | |                   #
#        | |__) |   _| |_| |__   ___  _ __   | |__) | __ _ _ __ | |_  | |     ___ | | ___  _ __         #
#        |  ___/ | | | __| '_ \ / _ \| '_ \  |  ___/ '__| | '_ \| __| | |    / _ \| |/ _ \| '__|        #
#        | |   | |_| | |_| | | | (_) | | | | | |   | |  | | | | | |_  | |___| (_) | | (_) | |           #
#        |_|    \__, |\__|_| |_|\___/|_| |_| |_|   |_|  |_|_| |_|\__|  \_____\___/|_|\___/|_|           #
#                __/ |                                                                                  #
#               |___/                                                                                   #
#                                                                                                       #
#                                     -----------------------                                           #
#                                  Module created by @Nicorebo-18                                       #
#                                                                                                       #
#                                     Documentation & Examples:                                         #
#                       https://github.com/Nicorebo-18/Python-Print-With-Color                          #
#                                     -----------------------                                           #
#                                                                                                       #
#########################################################################################################



# Print colored text using 8-bit color codes and optional text styles.

def print_color_8bits(text, foreground="reset", background="reset", styles=[]):
    """
    Print colored text using 8-bit color codes and optional text styles.

    Parameters:
    - text (str): The text to be colored.
    - foreground (str, optional): The foreground color name or code (default is "reset").
    - background (str, optional): The background color name or code (default is "reset").
    - styles (list, optional): A list of text styles to apply (e.g., ["bold", "italic"]).

    Color and style codes are specified using string names or codes.
    Supported color names: "black", "red", "green", "yellow", "blue", "magenta", "cyan", "white", "default", "reset".
    Supported style names: "bold", "dim", "italic", "underline", "blink", "reverse", "hidden", "strikethrough".
    """
    color_codes = {
        "black": 0,
        "red": 1,
        "green": 2,
        "yellow": 3,
        "blue": 4,
        "magenta": 5,
        "cyan": 6,
        "white": 7,
        "default": 9,
        "reset": 0
    }

    style_codes = {
        "bold": 1,
        "dim": 2,
        "italic": 3,
        "underline": 4,
        "blink": 5,
        "reverse": 7,
        "hidden": 8,
        "strikethrough": 9
    }

    foreground_code = color_codes.get(foreground.lower(), 0)
    background_code = color_codes.get(background.lower(), 0)

    style_sequence = ";".join(str(style_codes.get(style.lower(), "")) for style in styles)
    
    escape_sequence = f"\x1b[{style_sequence};38;5;{foreground_code}m\x1b[48;5;{background_code}m"
    reset_sequence = "\x1b[0m"
    colored_text = f"{escape_sequence}{text}{reset_sequence}"

    print(colored_text)


# Print colored text using RGB color codes and optional text styles.

def print_color_rgb(text, foreground=None, background=None, styles=[]):
    """
    Print colored text using RGB color codes and optional text styles.

    Parameters:
    - text (str): The text to be colored.
    - foreground (tuple, optional): RGB values for the foreground color (default is None).
    - background (tuple, optional): RGB values for the background color (default is None).
    - styles (list, optional): A list of text styles to apply (e.g., ["bold", "italic"]).

    RGB values are specified as tuples with three integers in the range 0-255.
    Supported style names: "bold", "dim", "italic", "underline", "blink", "reverse", "hidden", "strikethrough".
    """
    style_codes = {
        "bold": 1,
        "dim": 2,
        "italic": 3,
        "underline": 4,
        "blink": 5,
        "reverse": 7,
        "hidden": 8,
        "strikethrough": 9
    }

    style_sequence = ";".join(str(style_codes.get(style.lower(), "")) for style in styles)
    escape_sequence = f"\033[{style_sequence}"
    
    if foreground:
        fg_r, fg_g, fg_b = foreground
        escape_sequence += f";38;2;{fg_r};{fg_g};{fg_b}"

    if background:
        bg_r, bg_g, bg_b = background
        escape_sequence += f";48;2;{bg_r};{bg_g};{bg_b}"

    escape_sequence += "m"
    reset_sequence = "\033[0m"
    colored_text = f"{escape_sequence}{text}{reset_sequence}"

    print(colored_text)

#    --------------         Example usage codes       ------------------
# print_color_8bits("Colored text example", foreground="red", background="white", styles=["italic", "underline"])
# print_color_rgb("RGB colored text example", styles=["bold", "strikethrough"])