from app.config.mysqlconnection import connectToMySQL
from flask import flash

class Book:
    db = 'books_schema'
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
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