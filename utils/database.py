from .database_connection import DatabaseConnection
from typing import List, Dict, Union

"""
Concerned with storing and retrieving books from a database.
"""
Book = Dict(str, Union(str, int))

DB_HOST = "data.db"

class Database:
    """A class used to interact with the database of the library.
    ...
    Attributes
    ----------
    DB_HOST : str
        The database host (default "db.host").
    
    """

    DB_HOST = "data.db"

    @classmethod
    def create_book_table(cls) -> None:
        """Creates a book table if it doesn't already exist."""

        with DatabaseConnection(cls.DB_HOST) as connection:
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)")

    @classmethod
    def add_book(cls, name: str, author: str) -> None:
        """Adds a book to the books table.
        
        Parameters
        ----------
        name : str
            The name of the book to be added.
        author : str
            The name of the author of the book.
        """

        with DatabaseConnection(cls.DB_HOST) as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO books VALUES(?, ?, 0)", (name, author))

    @classmethod
    def get_all_books(cls) -> List[Book]:
        """Gets all the books of the library."""

        with DatabaseConnection(cls.DB_HOST) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM books")
            books = [{"name": row[0], "author": row[1], "read": row[2]} for row in cursor.fetchall()] # [(name, author, read), (name, author, read)]

        return books

    @classmethod
    def mark_book_as_read(cls, name: str) -> None:
        """Marks a book as read.

        Parameters
        ----------
        name : str
            The name of the book to be marked as read.
        """

        with DatabaseConnection(cls.DB_HOST) as connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE books SET read=? WHERE name=?", (1, name))

    @classmethod
    def delete_book(cls, name: str) -> None:
        """Deletes a book.

        Parameters
        ----------
        name : str
            The name of the book to be deleted.
        """

        with DatabaseConnection(cls.DB_HOST) as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM books WHERE name=?", (name,))