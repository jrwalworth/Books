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
        pass
    
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
        pass
    
    @classmethod
    def update_book(cls, data):
        pass
    
    @classmethod
    def delete_book(cls, data):
        pass
    