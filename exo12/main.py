class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

    def display_book(self):
        print(f"{self.title} by {self.author} year: {self.year} borrowed: {self.is_borrowed}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        print(f"=========== add book ===================== ")
        self.books.append(book)
        print(f"Book added: {book.title} by {book.author} ({book.year})")
        return

    def remove_book(self, book_title):
        print(f"=========== remove book ===================== ")
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                print("Book removed: ")
                book.display_book()
                return
        print("Book not found")

    def borrow_book(self, book_title):
        print(f"=========== borrow book ===================== ")
        for book in self.books:
            if book.title == book_title:
                book.is_borrowed = True
                print("Book borrowed: ")
                book.display_book()
                return
        print("Book not found")

    def return_book(self, book_title):
        print(f"=========== return book ===================== ")
        for book in self.books:
            if book.title == book_title:
                book.is_borrowed = False
                print("Book retuned: ")
                book.display_book()
                return
        print("Book not found")

    def list_available_books(self):
        print(f"=========== available_books ===================== ")
        for book in self.books:
            if not book.is_borrowed:
                book.display_book()

    def list_all_books(self):
        print(f"=========== All books ===================== ")
        for book in self.books:
            book.display_book()
        return

    def list_borrowed_books(self):
        print(f"=========== borrowed_books ===================== ")
        for book in self.books:
            if book.is_borrowed:
                book.display_book()
        return


library = Library()
book = Book("Les Miserables", "Victor Hugo", 1862)
library.add_book(book)

book = Book("Marius", "Marcel Pagnol", 1929)
library.add_book(book)

book = Book("Fanny", "Marcel Pagnol", 1931)
library.add_book(book)

book = Book("Cesar", "Marcel Pagnol", 1936)
library.add_book(book)

book = Book("Germinal", "Emile Zola", 1867)
library.add_book(book)

book = Book("Justine", "Marquis de Sade", 1791)
library.add_book(book)

book = Book("Salammbo", "Gustave Flaubert", 1862)
library.add_book(book)

book = Book("Tartuffe", "Molière", 1664)
library.add_book(book)

library.list_all_books()

library.remove_book("Marius")
library.list_all_books()

library.borrow_book("Fanny")
library.list_all_books()

library.borrow_book("Cesar")
library.list_all_books()

library.list_available_books()
library.list_borrowed_books()

library.return_book("Cesar")
library.list_all_books()

library.list_available_books()
library.list_borrowed_books()