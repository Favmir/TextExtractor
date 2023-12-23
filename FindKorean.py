import tkinter as tk
from tkinter import IntVar
import re

def extract_korean(text, include_numbers):
    # Regular expression for matching Hangul characters, optionally including numbers, spaces, and punctuation
    if include_numbers:
        hangul_regex = re.compile(r'([\uac00-\ud7a3\d]+(?:[ \u3000\u303f\uff01-\uff0f\uff1a-\uff20\uff3b-\uff40\uff5b-\uff65]?[\uac00-\ud7a3\d]+)*)')
    else:
        hangul_regex = re.compile(r'([\uac00-\ud7a3]+(?:[ \u3000\u303f\uff01-\uff0f\uff1a-\uff20\uff3b-\uff40\uff5b-\uff65]?[\uac00-\ud7a3]+)*)')

    # Find all Korean text portions in the input text
    korean_parts = hangul_regex.findall(text)

    # Join the Korean parts into a single string, separated by newlines
    return '\n'.join(korean_parts)

def on_extract():
    input_text = text_input.get("1.0", tk.END)
    include_numbers = include_numbers_var.get()
    extracted_text = extract_korean(input_text, include_numbers)
    text_output.delete('1.0', tk.END)
    text_output.insert(tk.END, extracted_text)

root = tk.Tk()
root.title("Korean Text Extractor")

# Text input box
text_input = tk.Text(root, height=10, width=50)
text_input.pack()

# Checkbox for including numbers
include_numbers_var = IntVar()
checkbox = tk.Checkbutton(root, text="Include Numbers", variable=include_numbers_var)
checkbox.pack()

# Extract button
extract_button = tk.Button(root, text="Extract Korean Text", command=on_extract)
extract_button.pack()

# Text output box
text_output = tk.Text(root, height=10, width=50)
text_output.pack()

root.mainloop()
