class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} - {status}"


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

    def show_books(self):
        print(f"\n{self.name}'s Borrowed Books:")
        if len(self.borrowed_books) == 0:
            print("No books borrowed.")
        else:
            for book in self.borrowed_books:
                print(book.title)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, member, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                member.borrow(book)
                print(f"{member.name} borrowed '{book.title}'")
                return
        print("Book is not available.")

    def return_book(self, member, title):
        for book in member.borrowed_books:
            if book.title == title:
                book.available = True
                member.return_book(book)
                print(f"{member.name} returned '{book.title}'")
                return
        print("Book not found.")

    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            print(book)

    def __len__(self):
        return len(self.books)


library = Library()

book1 = Book("Python Basics", "John")
book2 = Book("C++ Programming", "Ali")
book3 = Book("Data Structures", "Sara")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

member1 = Member("Maryam")

library.display_books()

print("\nTotal Books:", len(library))

library.borrow_book(member1, "Python Basics")
library.borrow_book(member1, "Data Structures")

library.display_books()

member1.show_books()

library.return_book(member1, "Python Basics")

library.display_books()

member1.show_books()