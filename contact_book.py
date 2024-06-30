import tkinter as tk
from customtkinter import *
from tkinter import messagebox, simpledialog

# Initialize the main window
root = CTk()
root._set_appearance_mode("System")
root.title("Contact Book")
root.geometry("700x500")

contacts = {}

def add_contact():
    name = simpledialog.askstring("Input", "Enter contact name:")
    if name in contacts:
        messagebox.showerror("Error", "Contact already exists!")
        return
    phone = simpledialog.askstring("Input", "Enter phone number:")
    email = simpledialog.askstring("Input", "Enter email address:")
    contacts[name] = {'phone': phone, 'email': email}
    messagebox.showinfo("Success", "Contact added successfully!")
    view_contacts()

def view_contacts():
    listbox.delete(0, tk.END)
    for name, details in contacts.items():
        listbox.insert(tk.END, f"{name}: {details['phone']}, {details['email']}")

def search_contact():
    search_name = simpledialog.askstring("Input", "Enter contact name to search:")
    if search_name in contacts:
        details = contacts[search_name]
        messagebox.showinfo("Contact Found", f"Name: {search_name}\nPhone: {details['phone']}\nEmail: {details['email']}")
    else:
        messagebox.showerror("Error", "Contact not found!")

def update_contact():
    update_name = simpledialog.askstring("Input", "Enter contact name to update:")
    if update_name in contacts:
        new_phone = simpledialog.askstring("Input", "Enter new phone number:")
        new_email = simpledialog.askstring("Input", "Enter new email address:")
        contacts[update_name] = {'phone': new_phone, 'email': new_email}
        messagebox.showinfo("Success", "Contact updated successfully!")
        view_contacts()
    else:
        messagebox.showerror("Error", "Contact not found!")

def delete_contact():
    delete_name = simpledialog.askstring("Input", "Enter contact name to delete:")
    if delete_name in contacts:
        del contacts[delete_name]
        messagebox.showinfo("Success", "Contact deleted successfully!")
        view_contacts()
    else:
        messagebox.showerror("Error", "Contact not found!")

# Create GUI components
frame = CTkFrame(root)
frame.pack(pady=20)

button_style = {"font": ("Arial", 12, "bold"), "corner_radius": 10}

add_button = CTkButton(frame, text="Add Contact", command=add_contact, fg_color="#ff6f61", **button_style)
add_button.grid(row=0, column=0, padx=10, pady=10)

view_button = CTkButton(frame, text="View Contacts", command=view_contacts, fg_color="#48cae4", **button_style)
view_button.grid(row=0, column=1, padx=10, pady=10)

search_button = CTkButton(frame, text="Search Contact", command=search_contact, fg_color="#90be6d", **button_style)
search_button.grid(row=0, column=2, padx=10, pady=10)

update_button = CTkButton(frame, text="Update Contact", command=update_contact, fg_color="#ffb703", **button_style)
update_button.grid(row=0, column=3, padx=10, pady=10)

delete_button = CTkButton(frame, text="Delete Contact", command=delete_contact, fg_color="#f94144", **button_style)
delete_button.grid(row=0, column=4, padx=10, pady=10)

listbox = tk.Listbox(root, height=15, width=80, bg="#212121", fg="white", font=("Helvetica", 12), selectbackground="#4CAF50", selectforeground="white")
listbox.pack(pady=20)

# Start the main event loop
root.mainloop()
