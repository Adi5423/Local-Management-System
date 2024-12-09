from flask import Flask, render_template, redirect, url_for, request, jsonify
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
        if request.is_json:  # Check if the request is JSON
            data = request.json
            new_book = Book(data['title'], data['author'], data['isbn'])
        else:  # Handle form submission
            new_book = Book(request.form['title'], request.form['author'], request.form['isbn'])
        
        new_book.id = len(books) + 1  # Assign an ID
        books.append(new_book.__dict__)
        return redirect(url_for('list_books'))  # Redirect to the list page after adding

    return render_template('add_book.html')

@app.route('/books/edit/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    book = next((book for book in books if book['id'] == id), None)
    if not book:
        return render_template('error.html', message='Book not found'), 404

    if request.method == 'POST':
        if request.is_json:  # Check if the request is JSON
            data = request.json
            book['title'] = data.get('title', book['title'])
            book['author'] = data.get('author', book['author'])
            book['isbn'] = data.get('isbn', book['isbn'])
        else:  # Handle form submission
            book['title'] = request.form['title']
            book['author'] = request.form['author']
            book['isbn'] = request.form['isbn']
        return redirect(url_for('list_books'))

    return render_template('edit_book.html', book=book)

@app.route('/books/delete/<int:id>', methods=['POST'])
def delete_book(id):
    global books
    books = [book for book in books if book['id'] != id]
    return redirect(url_for('list_books'))

@app.route('/members/list')
def list_members():
    return render_template('list_members.html', members=members)

@app.route('/members/add', methods=['GET', 'POST'])
def add_member():
    if request.method == 'POST':
        if request.is_json:  # Check if the request is JSON
            data = request.json
            new_member = Member(data['name'], data['membership_id'])
        else:  # Handle form submission
            new_member = Member(request.form['name'], request.form['membership_id'])
        
        new_member.id = len(members) + 1  # Assign an ID
        members.append(new_member.__dict__)
        return redirect(url_for('list_members'))  # Redirect to the list page after adding

    return render_template('add_member.html')

@app.route('/members/edit/<int:id>', methods=['GET', 'POST'])
def edit_member(id):
    member = next((member for member in members if member['id'] == id), None)
    if not member:
        return render_template('error.html', message='Member not found'), 404

    if request.method == 'POST':
        if request.is_json:  # Check if the request is JSON
            data = request.json
            member['name'] = data.get('name', member['name'])
            member['membership_id'] = data.get('membership_id', member['membership_id'])
        else:  # Handle form submission
            member['name'] = request.form['name']
            member['membership_id'] = request.form['membership_id']
        return redirect(url_for('list_members'))

    return render_template('edit_member.html', member=member)

@app.route('/members/delete/<int:id>', methods=['POST', 'DELETE'])
def delete_member(id):
    global members
    members = [member for member in members if member['id'] != id]
    return redirect(url_for('list_members'))

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

@app.route('/crud', methods=['GET', 'POST'])
def crud_operations():
    return render_template('crud_operations.html')

if __name__ == '__main__':
    app.run(debug=True)