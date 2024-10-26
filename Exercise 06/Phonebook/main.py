class Contact:
    def __init__(self, name, phone, email):
        """Initialize a contact with a name, phone number, and email address."""
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        """Return string representation of the contact."""
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"


class Phonebook:
    def __init__(self):
        """Initialize an empty phonebook dictionary to store contacts."""
        self.contacts = {}  # Dictionary to hold contacts, with name as key

    def add_contact(self, contact):
        """Add a new contact to the phonebook."""
        self.contacts[contact.name] = contact  # Use contact name as key
        print(f"Added contact: {contact}")

    def remove_contact(self, name):
        """Remove a contact from the phonebook by name."""
        if name in self.contacts:
            removed_contact = self.contacts.pop(name)  # Remove contact from dictionary
            print(f"Removed contact: {removed_contact}")
        else:
            print(f"Contact with name '{name}' not found.")

    def search_contact(self, name):
        """Search for a contact by name and display its details."""
        contact = self.contacts.get(name)
        if contact:
            print(f"Found contact: {contact}")
        else:
            print(f"Contact with name '{name}' not found.")

    def display_all_contacts(self):
        """Display all contacts in the phonebook."""
        print("\nAll Contacts:")
        if self.contacts:
            for contact in self.contacts.values():
                print(contact)
        else:
            print("No contacts found.")

    def save_to_file(self, filename):
        """Save the contacts to a text file."""
        with open(filename, 'w') as file:
            for contact in self.contacts.values():
                file.write(f"{contact.name},{contact.phone},{contact.email}\n")  # Save contact details
        print(f"Contacts saved to '{filename}'.")

    def load_from_file(self, filename):
        """Load contacts from a text file into the phonebook."""
        try:
            with open(filename, 'r') as file:
                for line in file:
                    name, phone, email = line.strip().split(',')  # Split the line into attributes
                    contact = Contact(name, phone, email)  # Create a Contact object
                    self.add_contact(contact)  # Add contact to the phonebook
            print(f"Contacts loaded from '{filename}'.")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")


def main():
    """Main program loop for the phonebook."""
    phonebook = Phonebook()

    while True:
        print("\n--- Phonebook ---")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Search Contact")
        print("4. Display All Contacts")
        print("5. Save to File")
        print("6. Load from File")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            email = input("Enter contact email: ")
            contact = Contact(name, phone, email)
            phonebook.add_contact(contact)

        elif choice == '2':
            name = input("Enter contact name to remove: ")
            phonebook.remove_contact(name)

        elif choice == '3':
            name = input("Enter contact name to search: ")
            phonebook.search_contact(name)

        elif choice == '4':
            phonebook.display_all_contacts()

        elif choice == '5':
            filename = input("Enter filename to save contacts: ")
            phonebook.save_to_file(filename)

        elif choice == '6':
            filename = input("Enter filename to load contacts from: ")
            phonebook.load_from_file(filename)

        elif choice == '7':
            print("Exiting Phonebook. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
