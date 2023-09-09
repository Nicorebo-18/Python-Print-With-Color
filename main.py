def PrintColor8Bits(text, foreground="reset", background="reset", styles=[]):
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


def PrintColorRGB(text, foreground=(255, 255, 255), background=(0, 0, 0)):
    """
    Print colored text using RGB color codes.

    Parameters:
    - text (str): The text to be colored.
    - foreground (tuple, optional): RGB values for the foreground color (default is white).
    - background (tuple, optional): RGB values for the background color (default is black).

    RGB values are specified as tuples with three integers in the range 0-255.
    """
    fg_r, fg_g, fg_b = foreground
    bg_r, bg_g, bg_b = background

    escape_sequence = f"\033[38;2;{fg_r};{fg_g};{fg_b}m\033[48;2;{bg_r};{bg_g};{bg_b}m"
    reset_sequence = "\033[0m"
    colored_text = f"{escape_sequence}{text}{reset_sequence}"

    print(colored_text)


# Example usage:
PrintColor8Bits("Colored text example", foreground="red", background="white", styles=["italic", "underline"])
PrintColorRGB("RGB colored text example")
