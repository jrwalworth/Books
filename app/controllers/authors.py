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
def new_author():
    data = {
        'name' : request.form['name']
    }
    if not Author.v_add_author(request.form):
        return redirect('/authors')
    Author.create_author(data)
    flash(f'Success! Author {data["name"]} has been added to the database.')
    return redirect('/authors')

#show author page
@app.route('/authors/<int:id>/show')
def show_author(id):
    data = {
        'id': id,
    }
    all_books = Book.get_all()
    # Add author favorites to the show page
    author_faves = Author.get_author_faves(data)
    return render_template('show_author.html', author = Author.get_one(data),\
        all_books=all_books, author_faves=author_faves)


#add authors favorites from form
@app.route('/authors/fav', methods=['POST'])
def authors_fav(id):
    data = {
        'id': id,
    }
    Author.add_fav(data)
    return redirect('/authors/<int:id>/show', id=id)