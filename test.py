import pytest
from manager_book import BookManager
@pytest.fixture

def book_manager():
    """Crea una instancia de BookManager con una base de datos en memoria.""" 
    return BookManager()

def test_add_book(book_manager):
   book_manager.add_book("1984", "George Orwell", 1949)
   books = book_manager.get_all_books()
   assert len(books) == 1
   assert books[0].title == "1984"

def test_find_book_by_title(book_manager): 
    book_manager.add_book("1984", "George Orwell", 1949)
    result = book_manager.find_book("1984")
    assert len(result) == 1
    assert result[0].author == "George Orwell"

def test_find_book_by_author(book_manager):
    book_manager.add_book("1984", "George Orwell", 1949)
    result = book_manager.find_book("George Orwell")
    assert len(result) == 1
    assert result[0].title == "1984"

def test_delete_book(book_manager):
    book_manager.add_book("1984", "George Orwell", 1949)
    books = book_manager.get_all_books()
    assert len(books) == 1
    book_manager.delete_book(books[0].id)
    books = book_manager.get_all_books()
    assert len(books) == 0

def test_delete_non_existent_book(book_manager):
    with pytest.raises(ValueError):
        book_manager.delete_book(999)




