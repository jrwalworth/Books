from flask import render_template, redirect, request, flash
from app import app
from app.models.book import Book


@app.route('/books')
def books():
    all_books = Book.get_all()
    return render_template('books.html', all_books=all_books)


@app.route('/books/create', methods=['POST'])
def new_book():
    data = {
        'title' : request.form['title'],
        'num_of_pages' : request.form['num_of_pages'],
    }
    if not Book.v_add_book(request.form):
        return redirect('/books')
    Book.create_book(data)
    flash(f'Success! {data["title"]} book has been added to the database.')
    return redirect('/books')
