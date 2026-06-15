from storage.data import books
from storage.data import loans

from loans.models import Loan

def borrow_book(member_id, book_id):

    book = next(
        (
            b
            for b in books
            if b.id == book_id
        ),
        None
    )

    if not book:
        raise Exception("Book not found")

    if not book.is_available:
        raise Exception(
            "Book unavailable"
        )

    loan = Loan(
        member_id=member_id,
        book_id=book_id
    )

    loans.append(loan)

    book.is_available = False

    return loan
