import tkinter as tk
from tkinter import messagebox

class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {"Phone": phone, "Email": email, "Address": address}

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            return True
        else:
            return False

    def update_contact(self, name, phone, email, address):
        if name in self.contacts:
            self.contacts[name] = {"Phone": phone, "Email": email, "Address": address}
            return True
        else:
            return False

    def search_contact(self, search_term):
        found_contacts = {}
        for name, details in self.contacts.items():
            if search_term.lower() in name.lower() or search_term in details.values():
                found_contacts[name] = details
        return found_contacts

    def get_contact_list(self):
        return self.contacts

def add_contact_window():
    def add_contact():
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()

        if name.strip() == "":
            messagebox.showerror("Error", "Please enter a name.")
            return

        contact_manager.add_contact(name, phone, email, address)
        messagebox.showinfo("Success", "Contact added successfully.")
        clear_fields()

    add_contact_window = tk.Toplevel(root)
    add_contact_window.title("Add Contact")

    tk.Label(add_contact_window, text="Name:").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(add_contact_window, text="Phone:").grid(row=1, column=0, padx=10, pady=5)
    tk.Label(add_contact_window, text="Email:").grid(row=2, column=0, padx=10, pady=5)
    tk.Label(add_contact_window, text="Address:").grid(row=3, column=0, padx=10, pady=5)

    name_entry = tk.Entry(add_contact_window)
    name_entry.grid(row=0, column=1, padx=10, pady=5)
    phone_entry = tk.Entry(add_contact_window)
    phone_entry.grid(row=1, column=1, padx=10, pady=5)
    email_entry = tk.Entry(add_contact_window)
    email_entry.grid(row=2, column=1, padx=10, pady=5)
    address_entry = tk.Entry(add_contact_window)
    address_entry.grid(row=3, column=1, padx=10, pady=5)

    add_button = tk.Button(add_contact_window, text="Add Contact", command=add_contact)
    add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def clear_fields():
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)

def view_contact_list():
    contact_list_window = tk.Toplevel(root)
    contact_list_window.title("Contact List")

    contacts = contact_manager.get_contact_list()
    if not contacts:
        tk.Label(contact_list_window, text="No contacts found.").pack()
    else:
        for name, details in contacts.items():
            tk.Label(contact_list_window, text=f"Name: {name}, Phone: {details['Phone']}").pack()

def search_contact():
    def perform_search():
        search_term = search_entry.get()
        if search_term.strip() == "":
            messagebox.showerror("Error", "Please enter a search term.")
            return

        search_results = contact_manager.search_contact(search_term)
        if not search_results:
            messagebox.showinfo("Search Results", "No contacts found.")
        else:
            search_results_window = tk.Toplevel(root)
            search_results_window.title("Search Results")
            for name, details in search_results.items():
                tk.Label(search_results_window, text=f"Name: {name}, Phone: {details['Phone']}").pack()

    search_window = tk.Toplevel(root)
    search_window.title("Search Contact")

    search_entry = tk.Entry(search_window)
    search_entry.pack(padx=10, pady=5)

    search_button = tk.Button(search_window, text="Search", command=perform_search)
    search_button.pack(padx=10, pady=5)

def delete_contact_window():
    def delete_contact():
        name = delete_name_entry.get()
        if name.strip() == "":
            messagebox.showerror("Error", "Please enter a name.")
            return

        if contact_manager.delete_contact(name):
            messagebox.showinfo("Success", f"Contact '{name}' deleted successfully.")
            delete_name_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", f"Contact '{name}' not found.")

    delete_contact_window = tk.Toplevel(root)
    delete_contact_window.title("Delete Contact")

    tk.Label(delete_contact_window, text="Name:").pack(padx=10, pady=5)
    delete_name_entry = tk.Entry(delete_contact_window)
    delete_name_entry.pack(padx=10, pady=5)

    delete_button = tk.Button(delete_contact_window, text="Delete Contact", command=delete_contact)
    delete_button.pack(padx=10, pady=5)

# Create the main window
root = tk.Tk()
root.title("Contact Manager")

contact_manager = ContactManager()

# Create and place widgets
add_button = tk.Button(root, text="Add Contact", command=add_contact_window)
add_button.pack(padx=10, pady=5)

view_button = tk.Button(root, text="View Contact List", command=view_contact_list)
view_button.pack(padx=10, pady=5)

search_button = tk.Button(root, text="Search Contact", command=search_contact)
search_button.pack(padx=10, pady=5)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact_window)
delete_button.pack(padx=10, pady=5)

# Start the GUI event loop
root.mainloop()
