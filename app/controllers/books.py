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
    book = Book.get_all_favd(data)
    # all_authors = Author.get_all()
    return render_template('show_book.html', book = book,\
        all_authors = Author.get_all())


#add authors favorite book from form
@app.route('/books/fav', methods=['POST'])
def books_fav():
    data = {
        'author_id' : request.form['author_id'],
        'book_id' : request.form['book_id'],
    }
    Book.add_fav(data)
    return redirect(f'/books/{request.form["book_id"]}/show')