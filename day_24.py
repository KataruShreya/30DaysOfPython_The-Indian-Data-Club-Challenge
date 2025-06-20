from dataclasses import dataclass

@dataclass
class LibraryBooks:
    title: str
    author: str
    isbn: str
    publication_year: int

    def display_details(self) -> None:
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Publication Year: {self.publication_year}")

book = LibraryBooks(
    title="Harry Potter and the Philosopher's Stone",
    author="J.K. Rowling",
    isbn="978-0-7475-3269-9",
    publication_year=1997
)

book.display_details()


# CODE LOGIC


'''
1. We import the dataclass decorator from the dataclasses module:
   - @dataclass simplifies class creation by automatically generating methods like __init__, __repr__, and __eq__.

2. We define a class named LibraryBooks and decorate it with @dataclass:
   - This class represents a book in the library.
   - It contains four fields: title, author, isbn, and publication_year.

3. We define a method inside the class called display_details():
   - This method prints each attribute of the book in a clean format.
   - It's used to display book details when called.

4. We create an instance of LibraryBooks:
   - We pass in details of the book "Harry Potter and the Philosopher's Stone" such as title, author, ISBN, and publication year.

5. We call the display_details() method on the book instance:
   - This prints the book's information to the console in a readable form.

6. Result:
   - A simple and structured representation of a library book is displayed using the power of dataclasses.

'''

