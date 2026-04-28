import pytest
import os
import json
from library import add_book, list_books, update_status, remove_book, search_books, load_books, save_books
 
TEST_FILE = "books.json"
 
@pytest.fixture(autouse=True)
def clean_books():
    """Start each test with an empty books file."""
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    yield
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
 
def test_add_book():
    result = add_book("Divergent", "Veronica Roth", "Sci-Fi", "to-read")
    assert result is True
    books = load_books()
    assert len(books) == 1
    assert books[0]["title"] == "Divergent"
    assert books[0]["author"] == "Veronica Roth"
 
def test_add_duplicate_book():
    add_book("Divergent", "Veronica Roth", "Sci-Fi", "to-read")
    result = add_book("Divergent", "Veronica Roth", "Sci-Fi", "to-read")
    assert result is False
    books = load_books()
    assert len(books) == 1
 
def test_add_book_invalid_status():
    result = add_book("Divergent", "Veronica Roth", "Sci-Fi", "maybe")
    assert result is False
    books = load_books()
    assert len(books) == 0
 
def test_add_second_book():
    add_book("Divergent", "Veronica Roth", "Sci-Fi", "to-read")
    result = add_book("A Court of Thorns and Roses", "Sarah J. Maas", "Fantasy", "reading")
    assert result is True
    books = load_books()
    assert len(books) == 2
    assert books[1]["title"] == "A Court of Thorns and Roses"
    assert books[1]["author"] == "Sarah J. Maas"
 
def test_update_status():
    add_book("Divergent", "Veronica Roth", "Sci-Fi", "to-read")
    books = load_books()
    book_id = books[0]["id"]
    result = update_status(book_id, "reading")
    assert result is True
    books = load_books()
    assert books[0]["status"] == "reading"
 
def test_update_status_invalid():
    add_book("Divergent", "Veronica Roth", "Sci-Fi", "to-read")
    books = load_books()
    book_id = books[0]["id"]
    result = update_status(book_id, "maybe")
    assert result is False
 
def test_remove_book():
    add_book("Divergent", "Veronica Roth", "Sci-Fi", "to-read")
    books = load_books()
    book_id = books[0]["id"]
    result = remove_book(book_id)
    assert result is True
    books = load_books()
    assert len(books) == 0
 
def test_remove_book_not_found():
    result = remove_book(999)
    assert result is False
 
def test_search_books():
    add_book("Divergent", "Veronica Roth", "Sci-Fi", "to-read")
    add_book("A Court of Thorns and Roses", "Sarah J. Maas", "Fantasy", "reading")
    results = [b for b in load_books() if "divergent" in b["title"].lower()]
    assert len(results) == 1
    assert results[0]["title"] == "Divergent"
