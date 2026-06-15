import streamlit as st

from members.services import create_member
from books.services import create_book
from loans.services import borrow_book

st.title(
    "Mini Library System"
)
