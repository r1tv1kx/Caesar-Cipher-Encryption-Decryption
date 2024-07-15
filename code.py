import tkinter as tk
from tkinter import messagebox, ttk

# Caesar cipher logic
letters = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(text, key):
    ciphertext = ''
    for letter in text:
        letter = letter.lower()
        if letter == ' ':
            ciphertext += ' '
        elif letter in letters:
            index = letters.index(letter)
            new_index = (index + key) % 26
            ciphertext += letters[new_index]
        else:
            ciphertext += letter  # Handles non-alphabetic characters
    return ciphertext

def decrypt(ciphertext, key):
    text = ''
    for letter in ciphertext:
        letter = letter.lower()
        if letter == ' ':
            text += ' '
        elif letter in letters:
            index = letters.index(letter)
            new_index = (index - key) % 26
            text += letters[new_index]
        else:
            text += letter  # Handles non-alphabetic characters
    return text

# Function to handle button click
def perform_action():
    action = action_var.get()
    text = text_entry.get("1.0", tk.END).strip()
    key = key_entry.get().strip()

    # Validate key
    if not key.isdigit() or not (1 <= int(key) <= 26):
        messagebox.showerror("Invalid Key", "Key must be an integer between 1 and 26.")
        return

    key = int(key)

    # Perform encryption or decryption
    if action == "Encrypt":
        result = encrypt(text, key)
    elif action == "Decrypt":
        result = decrypt(text, key)
    else:
        messagebox.showerror("Invalid Action", "Please select a valid action.")
        return

    # Update result text box
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, result)

# Create the main window
root = tk.Tk()
root.title("Caesar Cipher")

# Configure styles
style = ttk.Style()
style.configure('TFrame', background='#f0f0f0')
style.configure('TLabel', background='#f0f0f0', font=('Helvetica', 12))
style.configure('TButton', background='#4CAF50', foreground='white', font=('Helvetica', 12, 'bold'))
style.configure('TRadiobutton', background='#f0f0f0', font=('Helvetica', 12))

# Main frame
main_frame = ttk.Frame(root, padding=20, style='TFrame')
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Action frame
action_frame = ttk.Labelframe(main_frame, text="Action", padding=10, style='TFrame')
action_frame.grid(row=0, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))

# Radio buttons for Encrypt/Decrypt
action_var = tk.StringVar(value="Encrypt")
encrypt_radio = ttk.Radiobutton(action_frame, text="Encrypt", variable=action_var, value="Encrypt", style='TRadiobutton')
decrypt_radio = ttk.Radiobutton(action_frame, text="Decrypt", variable=action_var, value="Decrypt", style='TRadiobutton')
encrypt_radio.grid(row=0, column=0, padx=10, pady=5)
decrypt_radio.grid(row=0, column=1, padx=10, pady=5)

# Key frame
key_frame = ttk.Frame(main_frame, padding=10, style='TFrame')
key_frame.grid(row=1, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))

ttk.Label(key_frame, text="Key (1-26):", font=('Helvetica', 12)).grid(row=0, column=0, padx=10, pady=5)
key_entry = ttk.Entry(key_frame, font=('Helvetica', 12))
key_entry.grid(row=0, column=1, padx=10, pady=5)

# Text entry frame
text_frame = ttk.Frame(main_frame, padding=10, style='TFrame')
text_frame.grid(row=2, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))

ttk.Label(text_frame, text="Enter text:", font=('Helvetica', 12)).grid(row=0, column=0, padx=10, pady=5)
text_entry = tk.Text(text_frame, height=10, width=40, font=('Helvetica', 12), background='#ffffff', foreground='#333333', borderwidth=2, relief="solid")
text_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Result frame
result_frame = ttk.Frame(main_frame, padding=10, style='TFrame')
result_frame.grid(row=3, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))

ttk.Label(result_frame, text="Result:", font=('Helvetica', 12)).grid(row=0, column=0, padx=10, pady=5)
result_text = tk.Text(result_frame, height=10, width=40, font=('Helvetica', 12), background='#ffffff', foreground='#333333', borderwidth=2, relief="solid")
result_text.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Perform Action button
action_button = ttk.Button(main_frame, text="Perform Action" , command=perform_action, style='TButton')
action_button.grid(row=4, column=0, columnspan=2, pady=10)
style.configure('TButton', foreground='black')
# Configure grid weights
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)

# Start the main loop
root.mainloop()
