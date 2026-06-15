import streamlit as st

from members.services import create_member
from books.services import create_book
from loans.services import borrow_book

st.title(
    "Mini Library System"
)
st.header("Register Member")

member_name = st.text_input(
    "Member Name"
)

if st.button("Add Member"):

    create_member(member_name)

    st.success(
        "Member created"
    )
st.header("Add Book")

book_title = st.text_input(
    "Book Title"
)

if st.button("Add Book"):

    create_book(book_title)

    st.success(
        "Book added"
    )
st.header("Borrow Book")

member_id = st.number_input(
    "Member ID",
    min_value=1
)

book_id = st.number_input(
    "Book ID",
    min_value=1
)

if st.button("Borrow"):

    borrow_book(
        member_id,
        book_id
    )

    st.success(
        "Book borrowed"
    )
