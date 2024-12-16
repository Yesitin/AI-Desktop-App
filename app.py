import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from ollama_script import ollama_procedure

# Function to load file
def upload_file():
    file_path = filedialog.askopenfilename(
        filetypes=[
            ("All files", "*.*"),
            ("PDF files", "*.pdf"),
            ("Word files", "*.docx"),
            ("Image files", "*.jpg *.jpeg *.png")
        ]
    )
    filepath_var.set(file_path)

# Function to run script
def run_file():
    user_input = input_input.get("1.0", tk.END).strip()
    filepath = filepath_var.get()
    result = ollama_procedure(user_input, filepath)
    output.delete(1.0, tk.END)
    output.insert(tk.END, result)

    

# tkinter GUI
root = tk.Tk()

root.geometry("700x610")
root.title("Local LLM")

# Color scheme for dark mode
bg_color = "#2E2E2E"
fg_color = "#E0E0E0"
highlight_color = "#444444"
root.configure(bg=bg_color)

# Input section
label_input = tk.Label(root, text = "Enter your question: ", font = ("Calibri Light", 12), bg = bg_color, fg = fg_color)
input_input = tk.Text(root, height= 3, width = 82, bg = highlight_color, fg = fg_color, insertbackground= "white")
label_input.pack(padx = 5, pady = 5)
input_input.pack(padx=5, pady=5)

# File upload
label_file = tk.Label(root, text = "Upload File: ", font = ("Calibri Light", 12), bg = bg_color, fg = fg_color)
filepath_var = tk.StringVar()
filepath_entry = tk.Entry(root, textvariable=filepath_var, width = 109, bg = highlight_color, fg= fg_color, insertbackground = "white")
file_button = tk.Button(root, text = "Upload", command = upload_file, bg=highlight_color, fg=fg_color, activebackground="#666666", activeforeground=fg_color)
label_file.pack(padx = 5, pady = 5)
filepath_entry.pack(padx=5, pady=5)
file_button.pack(padx=5, pady=5)

# Output section
output = scrolledtext.ScrolledText(root, width = 80, height = 20, bg = highlight_color, fg = fg_color, insertbackground = "white")
output.pack(padx=5, pady=25)
run_button = tk.Button(root, text = "Ask your Assistant", command = run_file, bg = highlight_color, fg=fg_color, activebackground="#666666", activeforeground=fg_color)
run_button.pack(padx=5, pady=0)

root.mainloop()
