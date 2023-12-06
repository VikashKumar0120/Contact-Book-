import os
import json

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=2)

def add_contact(contacts, name, phone, email, address):
    contacts[name] = {"phone": phone, "email": email, "address": address}
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully.")

def view_contact_list(contacts):
    if not contacts:
        print("Contact list is empty.")
    else:
        print("Contact List:")
        for name, contact_info in contacts.items():
            print(f"{name}: {contact_info['phone']}")

def search_contact(contacts, query):
    results = {}
    for name, contact_info in contacts.items():
        if query.lower() in name.lower() or query in contact_info["phone"]:
            results[name] = contact_info
    return results

def update_contact(contacts, name, phone, email, address):
    if name in contacts:
        contacts[name] = {"phone": phone, "email": email, "address": address}
        save_contacts(contacts)
        print(f"Contact '{name}' updated successfully.")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

def main():
    contacts = load_contacts()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address: ")
            add_contact(contacts, name, phone, email, address)

        elif choice == "2":
            view_contact_list(contacts)

        elif choice == "3":
            query = input("Enter name or phone number to search: ")
            results = search_contact(contacts, query)
            if results:
                print("\nSearch Results:")
                for name, contact_info in results.items():
                    print(f"{name}: {contact_info['phone']}")
            else:
                print("No results found.")

        elif choice == "4":
            name = input("Enter the name of the contact to update: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            address = input("Enter new address: ")
            update_contact(contacts, name, phone, email, address)

        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            delete_contact(contacts, name)

        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
