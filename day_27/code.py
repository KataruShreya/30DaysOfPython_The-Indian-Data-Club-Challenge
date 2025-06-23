from fastapi import FastAPI, HTTPException, Depends
from typing import List, Optional
from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session


engine = create_engine("sqlite:///./books.db")
LocalSession = sessionmaker(bind=engine)
Base = declarative_base()

# SQLAlchemy model
class BookModel(Base):
    __tablename__ = "books"
    book_id = Column(Integer, primary_key=True)
    title = Column(String(500))
    year = Column(Integer)
    author = Column(String)

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic schemas
class BookBase(BaseModel):
    title: str = Field(..., max_length=500, description="Title of the book")
    year: int = Field(..., description="Release year")
    author: str = Field(..., description="Name of the author")

class BookCreate(BookBase):
    pass

class Book(BookBase):
    book_id: int = Field(..., description="Unique identifier of the book")

    class Config:
        orm_mode = True

class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=500, description="Title of the book")
    year: Optional[int] = Field(None, description="Release year")
    author: Optional[str] = Field(None, description="Name of the author")


def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()


api = FastAPI()


# Endpoints
@api.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(BookModel).filter(BookModel.book_id == book_id).first()
    if book:
        return book
    raise HTTPException(status_code=404, detail="Book not found")


@api.get("/books/", response_model=List[Book])
def get_books(db: Session = Depends(get_db)):
    return db.query(BookModel).all()



@api.post("/books", response_model=Book)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    new_book = BookModel(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book



@api.patch("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: BookUpdate, db: Session = Depends(get_db)):
    book = db.query(BookModel).filter(BookModel.book_id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    for key, value in updated_book.dict(exclude_unset=True).items():
        setattr(book, key, value)
    db.commit()
    db.refresh(book)
    return book

@api.delete("/books/{book_id}", response_model=Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(BookModel).filter(BookModel.book_id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return book



# CODE LOGIC

'''

1. We import necessary modules:  
   - FastAPI, HTTPException, and Depends from fastapi to build the API, handle errors, and manage dependencies.  
   - BaseModel and Field from pydantic to define schemas with field validation.  
   - List and Optional from typing for type annotations.  
   - Column, Integer, String, and create_engine from sqlalchemy to define the DB schema and connect to the DB.  
   - declarative_base, sessionmaker, and Session from sqlalchemy.orm to configure and manage ORM models and DB sessions.

2. We initialize the FastAPI app:  
   - api = FastAPI() creates the application instance.

3. We set up the database connection:  
   - create_engine("sqlite:///./books.db") connects to a local SQLite database file.  
   - LocalSession = sessionmaker(bind=engine) creates session objects for database interaction.  
   - Base = declarative_base() is used as the base class for all ORM models.  
   - Base.metadata.create_all(bind=engine) ensures tables are created if they don't exist.

4. We define the SQLAlchemy model:  
   - BookModel maps to a table named "books" in the database.  
   - It has columns for book_id, title, year, and author.

5. We define the Pydantic schemas:  
   - BookBase: Contains common fields like title, year, and author with validation using Field().  
   - BookCreate: Inherits from BookBase and is used for adding new books.  
   - Book: Inherits from BookBase, adds a book_id field, and enables ORM mode using Config.orm_mode = True.  
   - BookUpdate: All fields are optional, allowing for partial updates during patching.

6. We define a dependency to handle database sessions:  
   - get_db() creates a database session, yields it for use in endpoints, and closes it afterward.

7. We define the GET endpoint /books/{book_id}:  
   - Searches for a book by its ID using a database query.  
   - If found, returns the book object. If not, raises a 404 error.

8. We define the GET endpoint /books/:  
   - Retrieves and returns a list of all books stored in the database.

9. We define the POST endpoint /books:  
   - Accepts a book payload and creates a new BookModel object.  
   - Adds the book to the database, commits the changes, and returns the newly added book.

10. We define the PATCH endpoint /books/{book_id}:  
    - Accepts partial updates for a book using the BookUpdate schema.  
    - Updates only the fields provided (exclude_unset=True) and commits the changes.  
    - Returns the updated book or a 404 error if not found.

11. We define the DELETE endpoint /books/{book_id}:  
    - Searches for the book by ID and deletes it from the database.  
    - Returns the deleted book or raises a 404 error if the book does not exist.

12. Result:  
    - A fully functional RESTful API for book management.  
    - Supports all CRUD operations: Create, Read, Update, Delete.  
    - Includes data validation, proper session handling, and automatic interactive documentation with Swagger UI.

'''
