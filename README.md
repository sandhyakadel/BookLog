# BookLog

## What is the tool?

BookLog is a command-line tool for managing your personal book collection. You can add books, track your reading status, search your library, and remove books you no longer want to track. All data is saved locally in a JSON file so your library is always available offline.

# Installation

Make sure you have Python 3.8 or higher installed. Then clone the repository and navigate into it:

    git clone https://github.com/sandhyakadel/BookLog.git
    cd BookLog

Install Pytest for any running tests

    pip install pytest

## Usage

Run the program using Python from inside the BookLog folder:

    python library.py <command>

# Commands

| Command | Description |
|--------|-------------|
| `add "<title>" "<author>" [genre] [status]` | Add a new book |
| `list [status]` | List all books, optionally filtered by status |
| `update <id> <status>` | Update a book's reading status |
| `remove <id>` | Remove a book by ID |
| `search "<query>"` | Search by title or author |

## Statuses

- `to-read` - books you want to read
- `reading` - books you are currently reading
- `finished` - books you finished reading

## Examples

**Add a Book:**
```bash
python library.py add "Divergent" "Veronica Roth" "Sci-Fi" "to-read"
```

**List all books:**
```bash
python library.py list
```

**List only books you are currently reading:**
```bash
python library.py list reading
```

**Update a book status:**
```bash
python library.py update 1 reading
```

**Search for a book:**
```bash
python library.py search "Veronica"
```

**Remove a book:**
```bash
python library.py remove 1
```

## Running Tests
```bash
pytest tests/
```
All 9 tests should pass.

## Known Limitations

- Book IDs are not reassigned after a book is removed, so gaps may appear in the ID list.
- There is no edit command to update a book's title or author after it has been added.
- Data is stored in a local `books.json` file and is not synced across devices.

# Future ideas

- A rating system for finished books could be added in the future
- A stats command showing reading progress is a planned future feature

