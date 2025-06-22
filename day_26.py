from fastapi import FastAPI, HTTPException
from typing import List, Optional
from pydantic import BaseModel, Field

api = FastAPI()

class BookBase(BaseModel):
    title: str = Field(..., max_length=500, description='Title of the book')
    year: int= Field(description='release year')
    author: str = Field(..., description='Name of the author')


class BookCreate(BookBase):
    pass

class Book(BookBase):
    book_id: int = Field(...,description= 'Unique identifier of the book')


class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=500, description='Title of the book')
    year: Optional[int] = Field(None, description='release year')
    author: Optional[str] = Field(None, description='Name of the author')



all_books = [
    Book(book_id=1, title="Harry Potter and the Philospher's Stone", year=1997, author="J.K Rowling"),
    Book(book_id=2, title="Harry Potter and the Goblet of Fire", year=2000, author="J.K Rowling")
]



@api.get('/books/{book_id}', response_model= Book)
def get_book(book_id: int):
    for book in all_books:
        if book.book_id == book_id:
            return book
        



@api.get('/books/', response_model=List[Book])
def get_books():
    return all_books


@api.post('/books', response_model= Book)
def create_book(book: BookCreate):
    new_book_id = max(book.book_id for book in all_books) + 1

    new_book = Book(book_id = new_book_id,
                    title = book.title,
                    year = book.year,
                    author = book.author)

    all_books.append(new_book)

    return new_book


@api.put('/books/{book_id}', response_model=Book)
def update_book(book_id: int, updated_book: BookUpdate):
    for book in all_books:
        if book.book_id == book_id:
            if updated_book.title is not None:
                book.title = updated_book.title
            if updated_book.year is not None:
                book.year = updated_book.year
            if updated_book.author is not None:    
                book.author = updated_book.author
            return book
    
    raise HTTPException(status_code=404, detail = "Book not found")

@api.delete('/books/{book_id}', response_model= Book)
def delete_book(book_id :int):
    for index, book in enumerate(all_books):
        if book.book_id == book_id:
            deleted_book = all_books.pop(index)
            return deleted_book
        
    raise HTTPException(status_code=404, detail = "Book not found")



# CODE LOGIC

'''

1. We import necessary modules:
   - FastAPI and HTTPException from fastapi to build and handle the API and errors.
   - BaseModel and Field from pydantic to define request and response schemas with validation.
   - List and Optional from typing to specify types for lists and optional fields.

2. We initialize the FastAPI app using:
   - api = FastAPI() to create an instance of the application.

3. We define data models using Pydantic:
   - BookBase: Base schema with fields title, year, and author.
     → Uses Field() for validation like max length and descriptions.
   - BookCreate: Inherits from BookBase, used specifically for creating new books.
   - Book: Extends BookBase by adding a book_id, used in responses.
   - BookUpdate: Allows optional updates to title, year, or author.

4. We create a mock database:
   - all_books is a list of Book objects representing a pre-filled in-memory database.

5. We define the endpoint /books/{book_id} (GET):
   - Retrieves a single book by its ID.
   - Iterates over all_books and returns the matching book.
   - If not found, raises a 404 error.

6. We define the endpoint /books/ (GET):
   - Returns the full list of books from all_books.

7. We define the endpoint /books (POST):
   - Accepts a new book via BookCreate.
   - Automatically assigns the next available book_id.
   - Appends the new book to all_books.
   - Returns the created book.

8. We define the endpoint /books/{book_id} (PUT):
   - Accepts updates using the BookUpdate model.
   - Searches for the book by ID and updates any fields provided.
   - Returns the updated book or raises 404 if not found.

9. We define the endpoint /books/{book_id} (DELETE):
   - Finds and removes a book by ID from all_books.
   - Returns the deleted book or raises a 404 error if not found.

10. Result:
   - A fully functional RESTful API for managing a library.
   - Supports all CRUD operations: Create, Read, Update, Delete.
   - Includes input validation, optional updates, and automatic documentation using FastAPI.

'''

