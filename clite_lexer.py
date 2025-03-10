import re
import tkinter as tk
from tkinter import scrolledtext

# Define token patterns
TOKEN_PATTERNS = [
    (r'\bint\b|\bbool\b|\bfloat\b|\bchar\b', 'TYPE'),
    (r'\btrue\b|\bfalse\b', 'BOOLEAN'),
    (r'\bif\b|\belse\b|\bwhile\b|\bmain\b', 'KEYWORD'),
    (r'==', 'EQU_OP'),
    (r'<=|>=|<|>', 'REL_OP'),
    (r'[+-]', 'ADD_OP'),
    (r'\*|/|%', 'MUL_OP'),
    (r'&&|\|\|', 'LOGICAL_OP'),
    (r'!', 'UNARY_OP'),
    (r'\(|\)|\{|\}|\[|\]|;', 'SYMBOL'),
    (r'\d+\.\d+', 'FLOAT'),
    (r'\d+', 'INTEGER'),
    (r'\'[a-zA-Z0-9]\'', 'CHAR'),
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'IDENTIFIER'),
    (r'=', 'ASSIGN_OP')
]

def tokenize(code):
    tokens = []
    while code:
        match = None
        for pattern, token_type in TOKEN_PATTERNS:
            regex = re.compile(pattern)
            match = regex.match(code)
            if match:
                tokens.append((match.group(), token_type))
                code = code[match.end():]
                break
        if not match:
            code = code[1:]
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
