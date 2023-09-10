# Python 3 Colorful Print Functions 🌈🖨️

These Python functions allow you to print text with various colors and styles in your terminal. Spice up your console output with these vibrant options! 🎨

With these functions, you can make your terminal output more engaging and colorful. Experiment with different colors and styles to create visually appealing text. 😊🚀

_Note: To ensure the proper functionality of these functions, it is important that your terminal supports the ANSI standard for colored text formatting. Make sure your console is ANSI-compatible before using these functions to achieve the desired effect._

#### Supported Python Versions
- Python 3.6+

---
## Installing

If you have pip on your system, you can simply install or upgrade the Python Module:

`pip install -U PythonPrintColors`

---
## Usage
To import the functions inside teh package simply use `from PythonPrintColors import *` as shown in the example:
```python
from PythonPrintColors import *

print_color_8bits("8 Bit colored text example", foreground="red", background="white", styles=["italic", "underline"])
print_color_rgb("RGB colored text example", foreground=(0, 128, 128), background=(0, 0, 128), styles=["underline"])
```

---
## Function: Print Color 8 Bits

`print_color_8bits` prints text using 8-bit color codes and optional text styles.

```python
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
```


##### Example Usage (8-bit Colors):

```python
# Example 1: Print 8-bit colored text with bold style and a custom background color (e.g., green)
print_color_8bits("Bold text with green background", foreground="white", background="green", styles=["bold"])

# Example 2: Print 8-bit colored text with italic style and a custom foreground color (e.g., yellow)
print_color_8bits("Italic text with yellow foreground", foreground="yellow", styles=["italic"])

# Example 3: Print 8-bit colored text with underline style, a custom foreground color (e.g., red),
# and a custom background color (e.g., blue)
print_color_8bits("Underlined text with red foreground and blue background", foreground="red", background="blue", styles=["underline"])
```

---

## Function: Print Color RGB 🌟

`print_color_rgb` prints text using RGB color codes and optional text styles.

```python
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
```

##### Example Usage (RGB Colors):

```python
# Example 4: Print RGB colored text with bold style and a custom background color (e.g., purple)
print_color_rgb("Bold text with purple background", foreground=(255, 255, 255), background=(128, 0, 128), styles=["bold"])

# Example 5: Print RGB colored text with italic style and a custom foreground color (e.g., orange)
print_color_rgb("Italic text with orange foreground", foreground=(255, 165, 0), styles=["italic"])

# Example 6: Print RGB colored text with underline style, a custom foreground color (e.g., teal),
# and a custom background color (e.g., navy blue)
print_color_rgb("Underlined text with teal foreground and navy blue background", foreground=(0, 128, 128), background=(0, 0, 128), styles=["underline"])
```