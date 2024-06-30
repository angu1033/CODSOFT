import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate the password
def generate_password():
    try:
        length = int(entry.get())
        if length <= 0:
            raise ValueError("Password length must be a positive integer")
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_label.config(text=password)
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.config(bg="#f0f0f0")

# Create and place the widgets in frames
header_frame = tk.Frame(root, bg="#4CAF50")
header_frame.pack(fill="both")

main_frame = tk.Frame(root, bg="#f0f0f0")
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

footer_frame = tk.Frame(root, bg="#4CAF50")
footer_frame.pack(fill="both")

# Header
header_label = tk.Label(header_frame, text="Password Generator", font=("Helvetica", 18, "bold"), bg="#4CAF50", fg="white")
header_label.pack(pady=10)

# Main content
tk.Label(main_frame, text="Enter the desired length of the password:", font=("Helvetica", 12), bg="#f0f0f0").pack(pady=10)
entry = tk.Entry(main_frame, font=("Helvetica", 12))
entry.pack(pady=5)

generate_button = tk.Button(main_frame, text="Generate Password", font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", command=generate_password)
generate_button.pack(pady=20)

password_label = tk.Label(main_frame, text="", font=("Helvetica", 14, "bold"), bg="#f0f0f0", fg="#333333")
password_label.pack(pady=10)

# Footer
footer_label = tk.Label(footer_frame, text="Created By Angad", font=("Helvetica", 10), bg="#4CAF50", fg="white")
footer_label.pack(pady=5)

# Start the main event loop
root.mainloop()
