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
        query = "SELECT * FROM authors WHERE id=%(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
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
        query = "INSERT INTO authors (name) VALUES (%(name)s);"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def update_author(cls, data):
        query = "UPDATE authors SET name=%(name)s, updated_at=Now() WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)
        
    @classmethod
    def delete_author(cls, data):
        query = "DELETE FROM authors WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def add_fav(cls, data):
        query = "INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_author_faves(cls, data):
        query = "SELECT a.*, f.*, b.* FROM authors a LEFT JOIN favorites f ON a.id = f.author_id\
            LEFT JOIN books b ON f.book_id = b.id WHERE a.id=%(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        
        
        auth_faves = []
        for af in results:
            auth_faves.append(af)
        return auth_faves
        
    #validate author form
    @staticmethod
    def v_add_author(author):
        is_valid = True
        if len(author['name']) < 1:
            is_valid = False
            flash('You must add an author name to proceed.')
        return is_valid