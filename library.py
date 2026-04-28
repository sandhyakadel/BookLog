import json
import os
import sys
from datetime import date

DATA_FILE = "books.json"

def load_books():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_books(books):
    with open(DATA_FILE, "w") as f:
        json.dump(books, f, indent=2)


def add_book(title, author, genre="Unknown", status="to-read"):
    valid_statuses = ["to-read", "reading", "finished"]
    if status not in valid_statuses:
        print(f"Error: status must be one of {valid_statuses}")
        return False

    books = load_books()

    for book in books:
        if book["title"].lower() == title.lower() and book["author"].lower() == author.lower():
            print(f"Error: '{title}' by {author} already exists.")
            return False

    book = {
        "id": len(books) + 1,
        "title": title,
        "author": author,
        "genre": genre,
        "status": status,
        "date_added": str(date.today()),
    }
    books.append(book)
    save_books(books)
    print(f"Added: '{title}' by {author} [{status}]")
    return True


def list_books(status_filter=None):
    books = load_books()

    if status_filter:
        books = [b for b in books if b["status"] == status_filter]

    if not books:
        print("No books found.")
        return

    print(f"\n{'ID':<5} {'Title':<30} {'Author':<20} {'Genre':<15} {'Status'}")
    print("-" * 80)
    for b in books:
        print(f"{b['id']:<5} {b['title']:<30} {b['author']:<20} {b['genre']:<15} {b['status']}")
    print(f"\nTotal: {len(books)} book(s)")


def update_status(book_id, new_status):
    valid_statuses = ["to-read", "reading", "finished"]
    if new_status not in valid_statuses:
        print(f"Error: status must be one of {valid_statuses}")
        return False

    books = load_books()
    for book in books:
        if book["id"] == book_id:
            book["status"] = new_status
            save_books(books)
            print(f"Updated '{book['title']}' to '{new_status}'")
            return True

    print(f"Error: No book with ID {book_id}")
    return False


def remove_book(book_id):
    books = load_books()
    for i, book in enumerate(books):
        if book["id"] == book_id:
            removed = books.pop(i)
            save_books(books)
            print(f"Removed: '{removed['title']}'")
            return True

    print(f"Error: No book with ID {book_id}")
    return False


def search_books(query):
    books = load_books()
    query_lower = query.lower()
    results = [
        b for b in books
        if query_lower in b["title"].lower() or query_lower in b["author"].lower()
    ]

    if not results:
        print(f"No books found matching '{query}'")
        return

    print(f"\n{'ID':<5} {'Title':<30} {'Author':<20} {'Genre':<15} {'Status'}")
    print("-" * 80)
    for b in results:
        print(f"{b['id']:<5} {b['title']:<30} {b['author']:<20} {b['genre']:<15} {b['status']}")
    print(f"\nFound: {len(results)} book(s)")


def main():
    if len(sys.argv) < 2:
        print("Commands: add, list, update, remove, search")
        return

    command = sys.argv[1].lower()

    if command == "add":
        if len(sys.argv) < 4:
            print('Usage: python library.py add "<title>" "<author>" [genre] [status]')
            return
        title = sys.argv[2]
        author = sys.argv[3]
        genre = sys.argv[4] if len(sys.argv) > 4 else "Unknown"
        status = sys.argv[5] if len(sys.argv) > 5 else "to-read"
        add_book(title, author, genre, status)

    elif command == "list":
        status_filter = sys.argv[2] if len(sys.argv) > 2 else None
        list_books(status_filter)

    elif command == "update":
        if len(sys.argv) < 4:
            print("Usage: python library.py update <id> <status>")
            return
        try:
            book_id = int(sys.argv[2])
        except ValueError:
            print("Error: ID must be a number")
            return
        update_status(book_id, sys.argv[3])

    elif command == "remove":
        if len(sys.argv) < 3:
            print("Usage: python library.py remove <id>")
            return
        try:
            book_id = int(sys.argv[2])
        except ValueError:
            print("Error: ID must be a number")
            return
        remove_book(book_id)

    elif command == "search":
        if len(sys.argv) < 3:
            print('Usage: python library.py search "<query>"')
            return
        search_books(sys.argv[2])

    else:
        print(f"Unknown command: '{command}'. Commands: add, list, update, remove, search")


if __name__ == "__main__":
    main()
