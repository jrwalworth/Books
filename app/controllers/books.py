from flask import render_template, redirect, request, flash
from app import app
from app.models.book import Book
from app.models.author import Author


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

#show author page
@app.route('/books/<int:id>/show')
def show_book(id):
    data = {
        'id': id,
    }
    # Add author favorites to the show page
    # author_faves = Author.get_author_faves(data)
    all_authors = Author.get_all()
    return render_template('show_book.html', book = Book.get_one(data),\
        all_authors = Author.get_all())
