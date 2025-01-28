import tkinter as tk
from tkinter import messagebox, scrolledtext
import random
import string

# Function to generate a password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4")
            return
        
        characters = ""
        if use_digits.get():
            characters += string.digits
        if use_special_chars.get():
            characters += string.punctuation
        characters += string.ascii_letters  # Always include letters
        
        password = "".join(random.sample(characters, length))
        password_display.delete(0, tk.END)
        password_display.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Enter a valid password length")

# Function to save password
def save_password():
    password = password_display.get()
    purpose = password_purpose_entry.get()
    if password and purpose:
        with open("passwords.txt", "a") as file:
            file.write(f"{purpose}: {password}\n")
        messagebox.showinfo("Success", "Password saved successfully!")
    else:
        messagebox.showerror("Error", "Enter password purpose before saving.")

# Function for text editor
def save_text():
    content = text_area.get("1.0", tk.END).strip()
    if content:
        with open("notes.txt", "w") as file:
            file.write(content)
        messagebox.showinfo("Success", "Text saved successfully!")
    else:
        messagebox.showerror("Error", "Nothing to save.")

# GUI Setup
root = tk.Tk()
root.title("Password Generator & Text Editor")
root.geometry("500x500")
root.configure(bg="#FFDDC1")  # Bright background color

# Password Generator Frame
password_frame = tk.LabelFrame(root, text="Password Generator", padx=10, pady=10, bg="#FFABAB", fg="black")
password_frame.pack(padx=10, pady=10, fill="both")

tk.Label(password_frame, text="Enter Password Length:", bg="#FFABAB", fg="black").grid(row=0, column=0)
length_entry = tk.Entry(password_frame, bg="#FFC3A0", fg="black")
length_entry.grid(row=0, column=1)

use_digits = tk.BooleanVar()
use_special_chars = tk.BooleanVar()
tk.Checkbutton(password_frame, text="Include Numbers", variable=use_digits, bg="#FFABAB", fg="black").grid(row=1, column=0)
tk.Checkbutton(password_frame, text="Include Special Characters", variable=use_special_chars, bg="#FFABAB", fg="black").grid(row=1, column=1)

tk.Label(password_frame, text="Password Purpose:", bg="#FFABAB", fg="black").grid(row=2, column=0)
password_purpose_entry = tk.Entry(password_frame, bg="#FFC3A0", fg="black")
password_purpose_entry.grid(row=2, column=1)

password_display = tk.Entry(password_frame, width=30, bg="#FFC3A0", fg="black")
password_display.grid(row=3, column=0, columnspan=2)

password_button = tk.Button(password_frame, text="Generate Password", command=generate_password, bg="#FF677D", fg="white")
password_button.grid(row=4, column=0)

save_password_button = tk.Button(password_frame, text="Save Password", command=save_password, bg="#FF677D", fg="white")
save_password_button.grid(row=4, column=1)

# Text Editor Frame
editor_frame = tk.LabelFrame(root, text="Text Editor", padx=10, pady=10, bg="#FFABAB", fg="black")
editor_frame.pack(padx=10, pady=10, fill="both", expand=True)

text_area = scrolledtext.ScrolledText(editor_frame, width=50, height=10, wrap=tk.WORD, bg="#FFC3A0", fg="black")
text_area.pack()

save_text_button = tk.Button(editor_frame, text="Save Text", command=save_text, bg="#FF677D", fg="white")
save_text_button.pack()

root.mainloop()
