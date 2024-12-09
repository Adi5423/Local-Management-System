from flask import Flask, render_template, redirect, url_for, request
from models import Book, Member

app = Flask(__name__)

# In-memory data storage
books = []
members = []

@app.route('/')
def index():
    return render_template('index.html', books_count=len(books), members_count=len(members))

@app.route('/books/list')
def list_books():
    return render_template('list_books.html', books=books)

@app.route('/books/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        new_book = Book(request.form['title'], request.form['author'], request.form['isbn'])
        new_book.id = len(books) + 1
        books.append(new_book.__dict__)
        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/members/add', methods=['GET', 'POST'])
def add_member():
    if request.method == 'POST':
        new_member = Member(request.form['name'], request.form['membership_id'])
        new_member.id = len(members) + 1
        members.append(new_member.__dict__)
        return redirect(url_for('index'))
    return render_template('add_member.html')

@app.route('/members/list')
def list_members():
    return render_template('list_members.html', members=members)

@app.route('/books/search', methods=['GET', 'POST'])
def search_books():
    if request.method == 'POST':
        query = request.form['query']
        filtered_books = [
            book for book in books 
            if (query.lower() in book['title'].lower() or 
                query.lower() in book['author'].lower() or 
                query.lower() in book.get('isbn', '').lower())
        ]
        return render_template('search_books.html', results=filtered_books)
    return render_template('search_books.html', results=None)

if __name__ == '__main__':
    app.run(debug=True)