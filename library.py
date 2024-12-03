class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        self.borrowed_by = None

    def borrow_book(self, user):
        if self.is_borrowed:
            print("Already borrowed")
            return False

        self.is_borrowed = True
        self.borrowed_by = user
        return True

    def return_book(self):
        if not self.is_borrowed:
            return False
        
        self.is_borrowed = False
        self.borrowed_by = None
        return True


class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def borrow_book(self, book):
        return book.borrow_book(self)

    def return_book(self, book):
        return book.return_book()


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)


    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.is_borrowed:
                    self.books.remove(book)
                    return True
                else:
                    return False
        return False


    def search_book(self, query):
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

