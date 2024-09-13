from src.Book import Book
from src.User import User
from typing import List
from operator import indexOf


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
        list_of_isbn: List[str] = []
        for book in self.__books:
            list_of_isbn.append(book.get_isbn())
        if isbn not in list_of_isbn:
            new_book: Book = Book.Book(isbn, title, author)
            self.__books.append(new_book)

    # 1.2 List All Books
    def list_all_books(self) -> None:
        for book in self.__books:
            print(f"ISBN: {book.get_isbn()}, Title: {book.get_title()}, Author: {book.get_title()}")
        pass

    # 2.1 Check out book
    def check_out_book(self, isbn, dni, due_date) -> str:
        list_of_dni: List[str] = []
        list_of_isbn: List[str] = []
        for user in self.__users:
            list_of_dni.append(user.get_dni())
        for book in self.__books:
            list_of_isbn.append(book.get_isbn())
        if isbn in list_of_isbn and dni in list_of_dni:
            if self.__books[indexOf(list_of_isbn, isbn)].is_aviable:
                self.__books[indexOf(list_of_isbn, isbn)].set_aviable(False)
                self.__checked_out_books.append(self.__books[indexOf(list_of_isbn, isbn)])
                self.__users[indexOf(list_of_dni, dni)].increment_checkouts()
                return f"User {dni} checked out book {isbn}"
            else:
                return f"Book {isbn} is not available"
        else:
            return f"Unable to find the data for the values: ISBN {isbn} and DNI: {dni}"

    # 2.2 Check in book
    def check_in_book(self, isbn, dni, returned_date) -> str:
        list_of_isbn: List[str] = []
        list_of_dni: List[str] = []
        for book in self.__books:
            list_of_isbn.append(book.get_isbn())
        for user in self.__users:
            list_of_dni.append(user.get_dni())
        if isbn in list_of_isbn and self.__books[indexOf(list_of_isbn, isbn)].is_aviable():
            self.__books[indexOf(list_of_isbn, isbn)].set_aviable(True)
            self.__checked_out_books.remove(self.__books[indexOf(list_of_isbn, isbn)])
            self.__checked_in_books.append(self.__books[indexOf(list_of_isbn, isbn)])
            self.__users[indexOf(list_of_dni, dni)].increment_checkins()
            return f"User {dni} checked out book {isbn}"
        return f"Book {isbn} is not available"

    # Utils
    def add_user(self, dni: str, name: str) -> None:
        list_of_dni: List[str] = []
        for user in self.__users:
            list_of_dni.append(user.get_dni())
        if dni not in list_of_dni:
            self.__users.append(User.User(dni, name))
        pass

