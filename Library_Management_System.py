
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Book '{title}' added successfully!")

    def show_books(self):
        if not self.books:
            print("No books available.")
            return

        for i, book in enumerate(self.books, start=1):
            status = "Issued" if book.is_issued else "Available"
            print(f"{i}. {book.title} by {book.author} - {status}")

    def issue_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_issued:
                    book.is_issued = True
                    print(f"'{book.title}' issued successfully!")
                else:
                    print("This book is already issued.")
                return

        print("Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_issued:
                    book.is_issued = False
                    print(f"'{book.title}' returned successfully!")
                else:
                    print("This book was not issued.")
                return

        print("Book not found.")


library = Library()

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        library.add_book(title, author)

    elif choice == "2":
        library.show_books()

    elif choice == "3":
        title = input("Enter book title to issue: ")
        library.issue_book(title)

    elif choice == "4":
        title = input("Enter book title to return: ")
        library.return_book(title)

    elif choice == "5":
        print("Exiting Library Management System.")
        break

    else:
        print("Invalid choice. Try again.")
