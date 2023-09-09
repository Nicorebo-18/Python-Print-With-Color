# Python 3 Colorful Print Functions 🌈🖨️

These Python functions allow you to print text with various colors and styles in your terminal. Spice up your console output with these vibrant options! 🎨

With these functions, you can make your terminal output more engaging and colorful. Experiment with different colors and styles to create visually appealing text. 😊🚀

## Function: Print Color 8 Bits

`PrintColor8Bits` prints text using 8-bit color codes and optional text styles.

```python
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
```

#### Example Usage:

```python
PrintColor8Bits("Colored text example", foreground="red", background="white", styles=["italic", "underline"])
```

## Function: Print Color RGB 🌟

`PrintColorRGB` prints text using RGB color codes and optional text styles.

```python
def PrintColorRGB(text, foreground=None, background=None, styles=[]):
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
```

#### Example Usage:

```python
PrintColorRGB("RGB colored text example", styles=["bold", "strikethrough"])
```