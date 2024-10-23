from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Crear la base de datos
engine = create_engine('sqlite:///books.db')
Base = declarative_base()

# Definir la clase que representa un libro
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=False)

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)

# # Crear una sesión para interactuar con la base de datos
# Session = sessionmaker(bind=engine)
# session = Session()

class BookManager:

    def __init__(self):
        self.engine = engine
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

# métodos para gestionar los libros
    def add_book(self, title, author, year):
        book = Book(title=title, author=author, year=year)
        self.session.add(book)
        self.session.commit()

    def get_all_books(self):
        return self.session.query(Book).all()

    def find_book(self, query):
        return self.session.query(Book).filter(Book.title.like(f'%{query}%') | Book.author.like(f'%{query}%')).all()

    def delete_book(self, book_id):
        book = self.session.query(Book).get(book_id)
        self.session.delete(book)
        self.session.commit()
