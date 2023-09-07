def ColorRGB(text, foreground=(255, 255, 255), background=(0, 0, 0)):
    fg_r, fg_g, fg_b = foreground
    bg_r, bg_g, bg_b = background

    escape_sequence = f"\033[38;2;{fg_r};{fg_g};{fg_b}m\033[48;2;{bg_r};{bg_g};{bg_b}m"
    reset_sequence = "\033[0m\n"
    colored_text = f"{escape_sequence}{text}{reset_sequence}"

    print(colored_text, end="")

if __name__ == "__main__":
    # Ejemplo de uso:
    ColorRGB("Texto con colores RGB")