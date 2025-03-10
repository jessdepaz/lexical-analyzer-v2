import re  # Import the 're' module for pattern matching and tokenizing the input code
import tkinter as tk  # Import tkinter for GUI creation
from tkinter import scrolledtext  # Import the scrolled text widget from tkinter

# Define regex patterns to identify different types of tokens in Clite code
TOKEN_PATTERNS = [
    (r'\bint\b|\bbool\b|\bfloat\b|\bchar\b', 'TYPE'),  # Matches C-like data types
    (r'\btrue\b|\bfalse\b', 'BOOLEAN'),  # Matches boolean values
    (r'\bif\b|\belse\b|\bwhile\b|\bmain\b', 'KEYWORD'),  # Matches common keywords
    (r'==', 'EQU_OP'),  # Matches equality operator
    (r'<=|>=|<|>', 'REL_OP'),  # Matches relational operators
    (r'[+-]', 'ADD_OP'),  # Matches addition and subtraction operators
    (r'\*|/|%', 'MUL_OP'),  # Matches multiplication, division, and modulo operators
    (r'&&|\|\|', 'LOGICAL_OP'),  # Matches logical AND (&&) and OR (||) operators
    (r'!', 'UNARY_OP'),  # Matches the NOT operator
    (r'\(|\)|\{|\}|\[|\]|;', 'SYMBOL'),  # Matches parentheses, brackets, and semicolons
    (r'\d+\.\d+', 'FLOAT'),  # Matches floating-point numbers
    (r'\d+', 'INTEGER'),  # Matches integer numbers
    (r'\'[a-zA-Z0-9]\'', 'CHAR'),  # Matches character literals
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'IDENTIFIER'),  # Matches variable names or function names
    (r'=', 'ASSIGN_OP')  # Matches the assignment operator
]

# Function to scan and tokenize the input code based on predefined patterns
def tokenize(code): 
    tokens = []  # List to store the matched tokens
    while code:
        match = None  # Variable to track if any pattern matches
        for pattern, token_type in TOKEN_PATTERNS:
            regex = re.compile(pattern)  # Compile the regex pattern
            match = regex.match(code)  # Try to match the pattern at the start of 'code'
            if match:  # If a match is found
                tokens.append((match.group(), token_type))  # Store the matched lexeme and its token type
                code = code[match.end():]  # Move the cursor forward in the input code
                break  # Exit the loop after a successful match
        if not match:  # If no match is found, skip the first character (to handle invalid characters)
            code = code[1:]
    return tokens  # Return the list of tokens

 # Function to get user input, tokenize it, and display the results in the output area
def analyze_code():
    code = input_area.get("1.0", tk.END).strip()  # Get text from the input field and remove extra spaces
    tokens = tokenize(code)  # Call tokenize() to extract tokens
    output_area.config(state=tk.NORMAL)  # Enable the output area for modifications
    output_area.delete("1.0", tk.END)  # Clear previous output
    for lexeme, token in tokens:  # Loop through all extracted tokens
        output_area.insert(tk.END, f"{lexeme}: {token}\n")  # Display tokenized result
    output_area.config(state=tk.DISABLED)  # Disable output area to prevent manual edits

root = tk.Tk()  # Create the main application window
root.title("Clite Lexical Analyzer")  # Set the window title
root.geometry("500x400")  # Set the window size

tk.Label(root, text="Enter Clite Code:").pack()  # Create a label above the input area
input_area = scrolledtext.ScrolledText(root, height=10)  # Create a text input area with a scrollbar
input_area.pack()

analyze_button = tk.Button(root, text="Analyze", command=analyze_code) # Create a button to trigger analysis
analyze_button.pack()

output_area = scrolledtext.ScrolledText(root, height=10, state=tk.DISABLED) # Output area for results
output_area.pack()

root.mainloop() # Run the Tkinter event loop to keep the application running
