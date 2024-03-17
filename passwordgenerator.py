import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password using random.choices()
    password = ''.join(random.choices(characters, k=length))
    
    return password

def generate_and_display_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
        password = generate_password(length)
        password_display.config(state='normal')
        password_display.delete(1.0, tk.END)
        password_display.insert(tk.END, password)
        password_display.config(state='disabled')
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive integer for the password length.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=5)

length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_and_display_password)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

password_display = tk.Text(root, height=3, width=30, state='disabled')
password_display.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Start the GUI event loop
root.mainloop()

