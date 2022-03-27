from flask import render_template, redirect, request, flash
from app import app
from app.models.book import Book


@app.route('/books')
def books():
    all_books = Book.get_all()
    return render_template('books.html', all_books=all_books)


@app.route('/books/create', methods=['POST'])
def new_book():
    return redirect('/books')
