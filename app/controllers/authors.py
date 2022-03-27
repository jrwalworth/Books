from flask import render_template, redirect, request, flash
from app.models.author import Author
from app.models.book import Book
from app import app


#home
@app.route('/')
def index():
    return render_template('index.html')

#authors page
@app.route('/authors')
def authors():
    all_authors = Author.get_all()
    return render_template('authors.html', all_authors = all_authors)

#create_author
@app.route('/authors/create', methods=['POST'])
def new_author(cls, data):
    redirect('/authors')