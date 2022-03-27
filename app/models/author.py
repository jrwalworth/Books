from app.config.mysqlconnection import connectToMySQL
from flask import flash

class Author:
    db = 'books_schema'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_one(cls, data):
        pass
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL(cls.db).query_db(query)
        authors = []
        for a in results:
            authors.append(a)
        return authors

    @classmethod
    def create_author(cls, data):
        pass
    
    @classmethod
    def update_author(cls, data):
        pass
    
    @classmethod
    def delete_author(cls, data):
        pass
    