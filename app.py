from utils.database import Database as db



class Library:
    """A class that creates a console User Interface for interacting with a library.
    
    Parameters
    ----------
    USER_CHOICE : str
        The menu prompt.
    """

    USER_CHOICE = """
ENTER: 
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """

    @classmethod
    def menu(cls):
        """Prompts user with console interface for interacting with library."""

        user_input = input(cls.USER_CHOICE)
        while user_input != "q":
            if user_input == "a":
                cls.prompt_add_book()
            elif user_input == "l":
                cls.list_books()
            elif user_input == "r":
                cls.prompt_read_book()
            elif user_input == "d":
                cls.prompt_delete_book()
            else:
                print("Unknown command. Please try again.")

            user_input = input(cls.USER_CHOICE)

    @classmethod
    def prompt_add_book(cls):
        """Prompts user to add a book."""

        name = input("Enter the new book name: ")
        author = input("Enter the new book author: ")

        db.add_book(name, author)

    @classmethod
    def list_books(cls):
        """Prints all books in library to console."""

        books = db.get_all_books()
        for book in books:
            read = "YES" if book["read"] else "NO"
            print(f"{book['name']} by {book['author']}, read: {read}")

    @classmethod
    def prompt_read_book(cls):
        """Prompts user to enter the book they read."""

        name = input("Enter the name of the book you just finished reading: ")

        db.mark_book_as_read(name)

    @classmethod
    def prompt_delete_book(cls):
        """Prompts user to enter the book they want to delete."""

        name = input("Enter the name of the book you just want to delete: ")

        db.delete_book(name)

# run if in script mode
if __name__ == "__main__":
    db.create_book_table()
    Library.menu()