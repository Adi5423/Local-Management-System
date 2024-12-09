from flask import jsonify, request
from app import app
from models import Book, Member

books = []
members = []

@app.route('/books/add', methods=['POST'])
def add_book():
    data = request.json
    new_book = Book(data['title'], data['author'], data['isbn'])
    new_book.id = len(books) + 1  # Assign an ID
    books.append(new_book.__dict__)
    return jsonify(new_book.__dict__), 201

@app.route('/books/get', methods=['GET'])
def get_books():
    return jsonify(books), 200

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.json
    book = next((book for book in books if book['id'] == id), None)
    if book:
        book.update(data)
        return jsonify(book), 200
    return jsonify({'error': 'Book not found'}), 404

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    books = [book for book in books if book['id'] != id]
    return jsonify({'message': 'Book deleted'}), 204
# Add more routes for other CRUD operations and members...

@app.route('/members', methods=['POST'])
def add_member():
    data = request.json
    new_member = Member(data['name'], data['membership_id'])
    new_member.id = len(members) + 1  # Assign an ID
    members.append(new_member.__dict__)
    return jsonify(new_member.__dict__), 201

@app.route('/members', methods=['GET'])
def get_members():
    return jsonify(members), 200

@app.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    member = next((member for member in members if member['id'] == id), None)
    return jsonify(member), 200 if member else 404

@app.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    data = request.json
    member = next((member for member in members if member['id'] == id), None)
    if member:
        member.update(data)
        return jsonify(member), 200
    return jsonify({'error': 'Member not found'}), 404

@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    global members
    members = [member for member in members if member['id'] != id]
    return jsonify({'message': 'Member deleted'}), 204

# search query test calling /books/search?query=
@app.route('/books/search', methods=['GET'])
def search_books():
    query = request.args.get('query', '').lower()
    filtered_books = [
        book for book in books 
        if (query in book['title'].lower() or 
            query in book['author'].lower() or 
            query in book.get('isbn', '').lower())
    ]
    return jsonify(filtered_books), 200
