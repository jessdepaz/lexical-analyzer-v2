import re
import tkinter as tk
from tkinter import scrolledtext

# Define token patterns
TOKEN_PATTERNS = [
     ('KEYWORD', r'\b(int|bool|float|char|if|else|while|return|true|false|main)\b'),
     ('IDENTIFIER', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
     ('INTEGER', r'\b\d+\b'),
     ('FLOAT', r'\b\d+\.\d+\b'),
     ('CHAR', r"'[^']'"),
     ('BOOLEAN', r'\b(true|false)\b'),
     ('OPERATOR', r'==|!=|<=|>=|[+\-*/%<>&|!=]'),
     ('DELIMITER', r'[;(),{}\[\]]'),
     ('STRING', r'".*?"'),
     ('WHITESPACE', r'\s+'),
     ('COMMENT', r'//.*'),
     ('UNKNOWN', r'.')
 ]

def tokenize(code):
    tokens = []
    for pattern, token_type in TOKEN_PATTERNS:
        for match in re.finditer(pattern, code):
            tokens.append((match.group(), token_type))
    return tokens

def analyze_code():
    code = input_area.get("1.0", tk.END).strip()
    tokens = tokenize(code)
    output_area.config(state=tk.NORMAL)
    output_area.delete("1.0", tk.END)
    for lexeme, token in tokens:
        output_area.insert(tk.END, f"{lexeme}: {token}\n")
    output_area.config(state=tk.DISABLED)

# Create GUI
root = tk.Tk()
root.title("Clite Lexical Analyzer")
root.geometry("500x400")

tk.Label(root, text="Enter Clite Code:").pack()
input_area = scrolledtext.ScrolledText(root, height=10)
input_area.pack()

analyze_button = tk.Button(root, text="Analyze", command=analyze_code)
analyze_button.pack()

output_area = scrolledtext.ScrolledText(root, height=10, state=tk.DISABLED)
output_area.pack()

root.mainloop()
