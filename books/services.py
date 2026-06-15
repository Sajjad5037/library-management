from storage.data import books
from books.models import Book

def create_book(title):

    book = Book(
        id=len(books) + 1,
        title=title
    )

    books.append(book)

    return book
