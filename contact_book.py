contacts = {}

while True:
    print("\n----- Contact Book -----")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Show All Contacts")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter name: ")
            phone = input("Enter phone number: ")

            contacts[name] = phone
            print("Contact added successfully!")

        elif choice == 2:
            name = input("Enter name to search: ")

            if name in contacts:
                print("Phone:", contacts[name])
            else:
                print("Contact not found.")

        elif choice == 3:
            name = input("Enter name to delete: ")

            if name in contacts:
                del contacts[name]
                print("Contact deleted successfully!")
            else:
                print("Contact not found.")

        elif choice == 4:
            if len(contacts) == 0:
                print("No contacts available.")
            else:
                print("\nContacts:")
                for name, phone in contacts.items():
                    print(name, ":", phone)

        elif choice == 5:
            print("Exiting Contact Book...")
            break

        else:
            print("Please enter a number between 1 and 5.")

    except ValueError:
        print("Invalid input! Please enter a number.")