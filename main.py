from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# -----------------------------
# Book Model
# -----------------------------
class Book(BaseModel):
    id: int
    book_name: str
    author: str
    publisher: str

# In-memory database
books_db = []

# -----------------------------
# CREATE
# -----------------------------
@app.post("/books/")
def create_book(book: Book):
    # Prevent duplicate IDs
    for b in books_db:
        if b.id == book.id:
            raise HTTPException(status_code=400, detail="Book ID already exists")
    books_db.append(book)
    return {"message": "Book added successfully", "book": book}

# -----------------------------
# READ ALL
# -----------------------------
@app.get("/books/")
def get_books():
    return books_db

# -----------------------------
# READ ONE
# -----------------------------
@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# -----------------------------
# UPDATE
# -----------------------------
@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for index, book in enumerate(books_db):
        if book.id == book_id:
            books_db[index] = updated_book
            return {"message": "Book updated successfully", "book": updated_book}
    raise HTTPException(status_code=404, detail="Book not found")

# -----------------------------
# DELETE
# -----------------------------
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books_db):
        if book.id == book_id:
            deleted = books_db.pop(index)
            return {"message": "Book deleted successfully", "book": deleted}
    raise HTTPException(status_code=404, detail="Book not found")

