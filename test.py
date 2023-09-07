def rgb_to_hex(rgb):
    # Asegúrate de que los valores RGB estén en el rango válido (0-255)
    r, g, b = [max(0, min(255, int(x))) for x in rgb]
    # Convierte los valores RGB a formato hexadecimal y los concatena
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

# Ejemplo de uso
rgb_color = (255, 128, 0)  # Color naranja
hex_color = rgb_to_hex(rgb_color)
print("Color RGB:", rgb_color)
print("Color Hexadecimal:", hex_color)