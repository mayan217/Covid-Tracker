class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def delete_contact(self, contact):
        self.contacts.remove(contact)

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def display_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone Number: {contact.phone_number}, Email: {contact.email}")

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for contact in self.contacts:
                f.write(f"{contact.name},{contact.phone_number},{contact.email}\n")

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                data = line.strip().split(',')
                self.add_contact(Contact(data[0], data[1], data[2]))

def main():
    address_book = AddressBook()

    while True:
        print("\nAddress Book Menu:")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Display All Contacts")
        print("5. Save Contacts to File")
        print("6. Load Contacts from File")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact = Contact(name, phone_number, email)
            address_book.add_contact(contact)

        elif choice == '2':
            name = input("Enter name to delete: ")
            contact = address_book.search_contact(name)
            if contact:
                address_book.delete_contact(contact)
                print("Contact deleted successfully.")
            else:
                print("Contact not found.")

        elif choice == '3':
            name = input("Enter name to search: ")
            contact = address_book.search_contact(name)
            if contact:
                print(f"Name: {contact.name}, Phone Number: {contact.phone_number}, Email: {contact.email}")
            else:
                print("Contact not found.")

        elif choice == '4':
            address_book.display_contacts()

        elif choice == '5':
            filename = input("Enter filename to save: ")
            address_book.save_to_file(filename)
            print("Contacts saved to file.")

        elif choice == '6':
            filename = input("Enter filename to load: ")
            address_book.load_from_file(filename)
            print("Contacts loaded from file.")

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
