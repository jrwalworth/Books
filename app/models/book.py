from app.config.mysqlconnection import connectToMySQL
from flask import flash
from app.models import author

class Book:
    db = 'books_schema'
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.auth_have_favd = []
        
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM books WHERE id=%(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL(cls.db).query_db(query)
        all_books = []
        for book in results:
            all_books.append(book)
        return all_books
    
    @classmethod
    def get_all_favd(cls, data):
        query = "SELECT * FROM books b LEFT JOIN favorites f ON b.id = f.book_id\
            LEFT JOIN authors a ON f.author_id = a.id WHERE b.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        book = cls(results[0])
        for r in results:
            if r['a.id'] == None:
                break
            data = {
                'id' : r['a.id'],
                'name' : r['name'],
                'created_at' : r['a.created_at'],
                'updated_at' : r['a.updated_at'],
            }
            book.auth_have_favd.append(author.Author(data))
        return book
    
    @classmethod
    def remove_favd_book(cls, data):
        pass

    @classmethod
    def create_book(cls, data):
        query = "INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_of_pages)s);"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def update_book(cls, data):
        query = "UPDATE books SET title=%(title)s, num_of_pages=%(num_of_pages)s WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
        
    @classmethod
    def delete_book(cls, data):
        query = "DELET FROM books WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)
    
    #validate book form
    @staticmethod
    def v_add_book(book):
        is_valid = True
        if len(book['title']) < 1:
            is_valid = False
            flash('You must add a book title.')
        if len(book['num_of_pages']) < 1:
            is_valid = False
            flash('A book must have more pages than this.')
        return is_valid