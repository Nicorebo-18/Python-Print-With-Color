def ColorPrint(text, style="0", color="37", background_color="37"):
    # Diccionario de colores en inglés a códigos ANSI
    color_codes = {
        "black": "30",
        "red": "31",
        "green": "32",
        "yellow": "33",
        "blue": "34",
        "magenta": "35",
        "cyan": "36",
        "white": "37",
    }

    # Diccionario de estilos a códigos ANSI
    style_codes = {
        "bold": "1",
        "italic": "3",
        "underline": "4",
        "blink": "5",
        "reverse": "7",
        "reset": "0",
    }

    # Verifica si se proporcionó un estilo y obtiene su código ANSI
    style_code = style_codes.get(style, "")

    # Verifica si se proporcionó un color de texto y obtiene su código ANSI
    color_code = color_codes.get(color, "")
    color_code = f"38;5;{color_code}" if color_code else ""

    # Verifica si se proporcionó un color de fondo y obtiene su código ANSI
    background_code = color_codes.get(background_color, "")
    background_code = f"48;5;{background_code}" if background_code else ""

    # Combina los códigos de estilo, color de texto y color de fondo
    code = ";".join(filter(None, [style_code, color_code, background_code]))

    # Aplica la secuencia de escape ANSI y muestra el texto
    if code:
        print(f"\033[{code}m{text}\033[0m")
    else:
        print(text)

# Ejemplo de uso:
#ColorPrint("Texto en rojo")

colors_to_test = [
    "black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"
]

styles_to_test = [
    "bold", "italic", "underline", "blink", "reverse"
]

# Prueba todos los colores y estilos
for style in styles_to_test:
    for color in colors_to_test:
        for background_color in colors_to_test:
            formatted_text = f"Style: {style}, Text Color: {color}, Background: {background_color}"
            ColorPrint(formatted_text, style=style, color=color)
