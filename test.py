def Color8Bits(text, foreground="reset", background="reset", styles=[]):
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
    reset_sequence = "\x1b[0m\n"
    colored_text = f"{escape_sequence}{text}{reset_sequence}"

    print(colored_text, end="")

if __name__ == "__main__":
    # Ejemplo de uso:
    Color8Bits("Texto con colores", foreground="red", styles=["bold", "underline"])
