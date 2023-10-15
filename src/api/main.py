from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Sample data (in-memory)
authors = {}
books = {}

class Author(BaseModel):
    name: str

class Book(BaseModel):
    name: str
    page_numbers: int
    author_id: int

@app.get("/")
def read_root():
    return {"status": "connected succesfully"}

# Authors API
@app.post("/authors/", response_model=Author)
def create_author(author: Author):
    author_id = len(authors) + 1
    authors[author_id] = author
    return {"name": author.name}

@app.get("/authors/{author_id}", response_model=Author)
def read_author(author_id: int):
    if author_id not in authors:
        raise HTTPException(status_code=404, detail="Author not found")
    return authors[author_id]

@app.get("/authors/", response_model=list[Author])
def list_authors():
    return list(authors.values())

@app.put("/authors/{author_id}", response_model=Author)
def update_author(author_id: int, author: Author):
    if author_id not in authors:
        raise HTTPException(status_code=404, detail="Author not found")
    authors[author_id] = author
    return authors[author_id]

@app.delete("/authors/{author_id}", response_model=Author)
def delete_author(author_id: int):
    if author_id not in authors:
        raise HTTPException(status_code=404, detail="Author not found")
    deleted_author = authors.pop(author_id)
    return deleted_author

# Books API
@app.post("/books/", response_model=Book)
def create_book(book: Book):
    book_id = len(books) + 1
    books[book_id] = book
    return {"name": book.name, "page_numbers": book.page_numbers, "author_id": book.author_id}

@app.get("/books/{book_id}", response_model=Book)
def read_book(book_id: int):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    return books[book_id]

@app.get("/books/", response_model=list[Book])
def list_books():
    return list(books.values())

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: Book):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    books[book_id] = book
    return books[book_id]

@app.delete("/books/{book_id}", response_model=Book)
def delete_book(book_id: int):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    deleted_book = books.pop(book_id)
    return deleted_book
