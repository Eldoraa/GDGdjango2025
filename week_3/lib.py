"""7. Library Class 
● Create a class Library that stores a list of book titles. 
● Add methods add_book() and show_books(). 
● Test by adding a few books and displaying them. """
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for b in self.books:
            print(b)

lib = Library()
lib.add_book("silence patience")
lib.add_book("atomic habits")
lib.show_books()