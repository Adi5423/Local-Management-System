import unittest
from app import app

class LibraryManagementSystemTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_book(self):
        response = self.app.post('/api/books', json={'title': 'Test Book', 'author': 'Test Author', 'isbn': '1234567890'})
        self.assertEqual(response.status_code, 201)

    def test_get_books(self):
        response = self.app.get('/api/books')
        self.assertEqual(response.status_code, 200)

    def test_search_books(self):
        response = self.app.get('/api/books/search?query=Test')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Book', response.get_data(as_text=True))

    def test_pagination(self):
        response = self.app.get('/api/books?page=1')
        self.assertEqual(response.status_code, 200)

    def test_invalid_book_addition(self):
        response = self.app.post('/api/books', json={'title': '', 'author': 'Test Author', 'isbn': '1234567890'})
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()