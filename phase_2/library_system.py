class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print("Book not found.")

    def __len__(self):
        return len(self.books)


library = Library()

library.add_book("Python Programming")
library.add_book("C++ Basics")
library.add_book("Java Fundamentals")

print("Total Books:", len(library))

library.remove_book("C++ Basics")

print("Total Books After Removing:", len(library))

for book in library.books:
    print(book)