# Data models for books and members
class Book:
    def __init__(self, title, author, isbn):
        self.id = None  # Will be set when added to the list
        self.title = title
        self.author = author
        self.isbn = isbn

class Member:
    def __init__(self, name, membership_id):
        self.id = None  # Will be set when added to the list
        self.name = name
        self.membership_id = membership_id