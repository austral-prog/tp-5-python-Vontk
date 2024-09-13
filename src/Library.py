from src.Book import Book
from src.User import User


from typing import List, Optional

class Library:
    def __init__(self) -> None:
        self.__books: List[Book] = []
        self.__users: List[User] = []
        self.__checked_out_books: List[List[str, int, str]] = []  # [ISBN, DNI, DUE_DATE]
        self.__checked_in_books: List[List[str, int, str]] = []   # [ISBN, DNI, RETURNED_DATE]

    # 1.1 Add Book
    def add_book(self, isbn: str, title: str, author: str) -> None:
        new_book = Book(isbn, title, author)
        self.__books.append(new_book)

    # 1.2 List All Books
    def list_all_books(self) -> None:
        for book in self.__books:
            print(str(book))

    # Utils
    def find_book_by_isbn(self, isbn: str) -> Optional[Book]:
        for book in self.__books:
            if book.get_isbn() == isbn:
                return book
        return None

    def find_user_by_dni(self, dni: int) -> Optional[User]:
        for user in self.__users:
            if user.get_dni() == dni:
                return user
        return None

    def add_user(self, dni: int, name: str) -> None:
        user = User(dni, name)
        self.__users.append(user)

    # 2.1 Check out book
    def check_out_book(self, isbn: str, dni: int, due_date: str) -> str:
        book = self.find_book_by_isbn(isbn)
        user = self.find_user_by_dni(dni)

        if not book or not user:
            return f"Unable to find the data for the values: ISBN {isbn} and DNI: {dni}"

        if not book.is_available():
            return f"Book {isbn} is not available"

        # Proceed to check out
        book.set_available(False)
        book.increment_checkout_num()
        user.increment_checkouts()
        self.__checked_out_books.append([isbn, dni, due_date])
        return f"User {dni} checked out book {isbn}"

    # 2.2 Check in book
    def check_in_book(self, isbn: str, dni: int, returned_date: str) -> str:
        book = self.find_book_by_isbn(isbn)
        if not book:
            return f"Book {isbn} is not available"

        # Check if the book is checked out by the user
        checked_out = next((entry for entry in self.__checked_out_books if entry[0] == isbn and entry[1] == dni), None)
        if not checked_out:
            return f"Book {isbn} is not available"

        # Proceed to check in
        book.set_available(True)
        user = self.find_user_by_dni(dni)
        if user:
            user.increment_checkins()
        self.__checked_out_books.remove(checked_out)
        self.__checked_in_books.append([isbn, dni, returned_date])
        return f"Book {isbn} checked in by user {dni}"
