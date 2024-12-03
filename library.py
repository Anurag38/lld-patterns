# Book class represents a book in the library with its details and borrowing status
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False  # Tracks if book is currently borrowed
        self.borrowed_by = None   # Reference to User who borrowed the book

    def borrow_book(self, user):
        # Attempt to borrow book if it's available
        if self.is_borrowed:
            print("Already borrowed")
            return False

        self.is_borrowed = True
        self.borrowed_by = user
        return True

    def return_book(self):
        # Return book if it was borrowed
        if not self.is_borrowed:
            return False
        
        self.is_borrowed = False
        self.borrowed_by = None
        return True


# User class represents a library member who can borrow and return books
class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def borrow_book(self, book):
        # Delegate the borrowing to Book class
        return book.borrow_book(self)

    def return_book(self, book):
        # Delegate the returning to Book class
        return book.return_book()


# Library class manages the collection of books and users
class Library:
    def __init__(self):
        self.books = []  # List of all books in library
        self.users = []  # List of registered users

    def add_book(self, book):
        # Add a new book to library collection
        self.books.append(book)

    def remove_book(self, isbn):
        # Remove book by ISBN if it exists and is not borrowed
        for book in self.books:
            if book.isbn == isbn:
                if not book.is_borrowed:
                    self.books.remove(book)
                    return True
                else:
                    return False
        return False

    def search_book(self, query):
        # Search books by author, title or ISBN (case insensitive)
        results = []
        for book in self.books:
            if query.lower() == book.author.lower() or query.lower() == book.title.lower() or query == book.isbn:
                results.append(book)
        
        if results:
            for book in results:
                if not book.is_borrowed:
                    status = "Available"
                else:
                    status = "Borrowed"
        else:
            print("No book found")    
        return results
