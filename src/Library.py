from src.Book import Book
from src.User import User
from typing import List

class Library:
    def __init__(self):
        self.__books: List[Book] = []
        self.__users: List[User] = []
        self.__checked_out_books: List[Book] = []
        self.__checked_in_books: List[Book] = []

    # Getters
    def get_books(self) -> List[Book]:
        return self.__books

    def get_users(self) -> List[User]:
        return self.__users

    def get_checked_out_books(self) -> List[Book]:
        return self.__checked_out_books

    def get_checked_in_books(self) -> List[Book]:
        return self.__checked_in_books

    # 1.1 Add Book
    def add_book(self, isbn: str, title: str, author: str) -> None:
        if not any(book.get_isbn() == isbn for book in self.__books):
            new_book = Book(isbn, title, author)
            self.__books.append(new_book)

    # 1.2 List All Books
    def list_all_books(self) -> None:
        for book in self.__books:
            print(book.__str__())
        pass

    # 2.1 Check out book
    def check_out_book(self, isbn: str, dni: int, due_date: str) -> str:
        list_of_dni: List[int] = []
        list_of_isbn: List[str] = []
        for user in self.__users:
            list_of_dni.append(user.get_dni())
        for book in self.__books:
            list_of_isbn.append(book.get_isbn())
        book_index: int = list_of_isbn.index(isbn)
        user_index: int = list_of_dni.index(dni)
        if isbn in list_of_isbn and dni in list_of_dni:
            if self.__books[book_index].is_available():
                self.__books[book_index].set_available(False)
                self.__checked_out_books.append(self.__books[book_index])
                self.__users[user_index].increment_checkouts()
                return f"User {dni} checked out book {isbn}"
            else:
                return f"Book {isbn} is not available"
        else:
            return f"Unable to find the data for the values: ISBN {isbn} and DNI: {dni}"

    # 2.2 Check in book
    def check_in_book(self, isbn: str, dni: int, returned_date: str) -> str:
        list_of_isbn: List[str] = []
        list_of_dni: List[int] = []
        for book in self.__books:
            list_of_isbn.append(book.get_isbn())
        for user in self.__users:
            list_of_dni.append(user.get_dni())
        book_index: int = list_of_isbn.index(isbn)
        user_index: int = list_of_dni.index(dni)
        if isbn in list_of_isbn and not self.__books[book_index].is_available():
            self.__books[book_index].set_available(True)
            self.__checked_out_books.remove(self.__books[book_index])
            self.__checked_in_books.append(self.__books[book_index])
            self.__users[user_index].increment_checkins()
            return f"Book {isbn} checked in by user {dni}"
        return f"Book {isbn} is not available"

    # Utils
    def add_user(self, dni: int, name: str) -> None:
        if not any(user.get_dni() == dni for user in self.__users):
            new_user = User(dni, name)
            self.__users.append(new_user)
