import unittest
from app import app, books, members
import json
from models import Book, Member

class LibraryManagementTests(unittest.TestCase):
    def setUp(self):
        """Set up test environment before each test"""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app
        self.client = app.test_client()
        
        # Create application context
        self.ctx = self.app.app_context()
        self.ctx.push()
        
        # Reset the global lists before each test
        global books, members
        books.clear()
        members.clear()

    def test_index_page(self):
        """Test the index page loads correctly"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Total Books:', response.data)
        self.assertIn(b'Total Members:', response.data)

    def test_add_book_form(self):
        """Test adding a book via form submission"""
        response = self.client.post('/books/add', data={
            'title': 'Test Book',
            'author': 'Test Author',
            'isbn': '1234567890'
        }, follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]['title'], 'Test Book')

    def test_add_book_api(self):
        """Test adding a book via API"""
        response = self.client.post('/books/add', 
            json={
                'title': 'API Book',
                'author': 'API Author',
                'isbn': '0987654321'
            },
            content_type='application/json',
            follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]['title'], 'API Book')

    def test_delete_book(self):
        # Add a book
        response = self.client.post('/books/add', data={
            'title': 'Book to Delete',
            'author': 'Author',
            'isbn': '3333333333'
        }, follow_redirects=True)
    
        self.assertEqual(len(books), 1, "Book was not added successfully")
        book_id = books[0]['id']
    
        # Delete attempt
        response = self.client.post(f'/books/delete/{book_id}', follow_redirects=True)
        self.assertEqual(len(books), 0, "Book was not deleted successfully")

    def test_add_member_form(self):
        """Test adding a member via form submission"""
        response = self.client.post('/members/add', data={
            'name': 'Test Member',
            'membership_id': 'MEM001'
        }, follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(members), 1)
        self.assertEqual(members[0]['name'], 'Test Member')

    def test_add_member_api(self):
        """Test adding a member via API"""
        response = self.client.post('/members/add', 
            json={
                'name': 'API Member',
                'membership_id': 'MEM002'
            },
            content_type='application/json',
            follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(members), 1)
        self.assertEqual(members[0]['name'], 'API Member')

    def test_edit_member(self):
        """Test editing a member"""
        # First add a member
        response = self.client.post('/members/add', data={
            'name': 'Original Name',
            'membership_id': 'MEM003'
        }, follow_redirects=True)
        
        self.assertEqual(len(members), 1)  # Verify member was added
        member_id = members[0]['id']
        
        # Then edit it
        response = self.client.post(f'/members/edit/{member_id}', data={
            'name': 'Updated Name',
            'membership_id': 'MEM004'
        }, follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(members[0]['name'], 'Updated Name')

    def test_search_books(self):
        """Test searching books"""
        # Add test books
        self.client.post('/books/add', data={
            'title': 'Python Programming',
            'author': 'John Doe',
            'isbn': '1234567890'
        })
        self.client.post('/books/add', data={
            'title': 'Java Programming',
            'author': 'Jane Smith',
            'isbn': '0987654321'
        })
        
        response = self.client.post('/books/search', data={'query': 'Python'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Python Programming', response.data)
        self.assertNotIn(b'Java Programming', response.data)

    def test_search_members(self):
        """Test searching members"""
        # Add test members
        self.client.post('/members/add', data={
            'name': 'John Smith',
            'membership_id': 'MEM006'
        })
        self.client.post('/members/add', data={
            'name': 'Jane Doe',
            'membership_id': 'MEM007'
        })
        
        response = self.client.post('/members/search', data={'query': 'John'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'John Smith', response.data)
        self.assertNotIn(b'Jane Doe', response.data)

if __name__ == '__main__':
    unittest.main()
    
