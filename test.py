def rgb_to_hex(rgb):
    r, g, b = [max(0, min(255, int(x))) for x in rgb]
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

def ColorPrint(text, hex_color, style=None):
    # Establece el código de escape ANSI para el color y estilo
    color_code = f"\x1b[38;2;{hex_color}m"
    style_code = f"\x1b[{style}m" if style else ""
    reset_code = "\x1b[0m"  # Restaura el estilo y color predeterminados

    # Combina los códigos y muestra el texto con el estilo y color especificados
    formatted_text = f"{color_code}{style_code}{text}{reset_code}"
    print(formatted_text)

# Ejemplo de uso:
rgb_color = (255, 128, 0)  # Color naranja
hex_color = rgb_to_hex(rgb_color)
print("\x1b[38;2;255;128;0mTRUECOLOR\x1b[0m\n")
ColorPrint("Texto en naranja", hex_color, style="1")  # Establece el estilo en negrita
