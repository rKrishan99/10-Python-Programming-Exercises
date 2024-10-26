import os # Imports the 'os' module to interact with the operating system,
           # such as checking if a file exists and creating files.

class Book:
    """Represents a Book with title, author, and ISBN."""
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        """Returns the string representation of a book."""
        return f"{self.title}, {self.author}, {self.isbn}"


class Library:
    """Handles library operations: adding, removing, and searching books."""
    def __init__(self, filename="books_details.txt"):
        self.filename = filename

        # Create the file if it doesn't exist
        if not os.path.exists(filename):
            open(filename, "w").close()

    def add_book(self, book):
        """Adds a new book to the library file."""
        with open(self.filename, "a") as file:
            file.write(str(book) + "\n")
        print(f"\n'{book.title}' has been added to the library.")

    def remove_book(self, isbn):
        """Removes a book by its ISBN from the library."""
        books = self._load_books()
        updated_books = [b for b in books if b.isbn != isbn]

        if len(books) == len(updated_books):
            print(f"\nNo book found with ISBN {isbn}.")
        else:
            self._save_books(updated_books)
            print(f"\nBook with ISBN {isbn} has been removed.")

    def search_book(self, keyword):
        """Searches for books based on a keyword in title or author."""
        books = self._load_books()
        found_books = [b for b in books if keyword.lower() in b.title.lower() or keyword.lower() in b.author.lower()]

        if found_books:
            print(f"\nBooks matching '{keyword}':")
            for book in found_books:
                print(book)
        else:
            print(f"\nNo books found for keyword '{keyword}'.")

    def _load_books(self):
        """Loads all books from the file."""
        books = []
        with open(self.filename, 'r') as file:
            for line in file:
                title, author, isbn = line.strip().split(", ")
                books.append(Book(title, author, isbn))
        return books

    def _save_books(self, books):
        """Saves the list of books to the file."""
        with open(self.filename, "w") as file:
            for book in books:
                file.write(f"{book}\n")


def get_book_details():
    """Prompts the user to enter book details."""
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    isbn = input("Enter ISBN: ")
    return Book(title, author, isbn)


def main():
    """Main function to handle the menu-driven interface."""
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. View All Books")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            # Add a new book
            book = get_book_details()
            library.add_book(book)

        elif choice == '2':
            # Remove a book by ISBN
            isbn = input("Enter ISBN of the book to remove: ")
            library.remove_book(isbn)

        elif choice == '3':
            # Search for a book
            keyword = input("Enter a keyword to search (title/author): ")
            library.search_book(keyword)

        elif choice == '4':
            # Display all books
            books = library._load_books()
            if books:
                print("\n--- List of Books ---")
                for book in books:
                    print(book)
            else:
                print("\nNo books available in the library.")

        elif choice == '5':
            # Exit the program
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
