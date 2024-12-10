# Library Management System

This is a simple **Library Management System** built using **Flask**, a lightweight web framework for Python. The application allows users to manage books and members, including adding, editing, deleting, and searching for both.

## Features
- **Book Management**: Add, edit, delete, and search for books.
- **Member Management**: Add, edit, delete, and search for members.
- **Data Storage**: Uses JSON files for data persistence.
- **User -Friendly Interface**: Simple HTML templates for interaction.

  
### Project Highlights
- **Efficient Book & Member Management**
- **JSON-based Persistent Storage**
- **Responsive Web Interface**
- **Comprehensive Test Coverage**


## Technologies Used
- **Flask**: Web framework for building the application.
- **HTML/CSS**: For the front-end user interface.
- **JSON**: For data storage.
- **Python**: Programming language used for the application logic.

## Installation

### Prerequisites
- **Python 3.x**
- **Flask** (Install via pip)

### Clone the Repository
To clone the repository, run the following command in your terminal:

```bash
git clone https://github.com/yourusername/library-management-system.git
```

Navigate to the Project Directory
```bash
cd library-management-system
```
Install Dependencies
If you haven't installed Flask yet, you can do so using pip:

```bash
pip install Flask
```
Running the Application
To run the application, execute the following command:

```bash
python app.py
```
The application will start, and you can access it in your web browser at http://127.0.0.1:5000/.

To save the Books and Members list in JSON file in root directory. 
Set the parameter :
```bash
#line 24
USE_JSON_STORAGE = True 
```
If want to use List Storing system without JSON for Books and Members.
Set the parameter :
```bash
#line 24
USE_JSON_STORAGE = False
```

## Application Structure -:
app.py: The main application file containing all the routes and logic.

models.py: Contains the Book and Member classes (not provided in the original code, but assumed to exist).

templates/: Directory containing HTML templates for rendering views.
books.json: JSON file for storing book data.

members.json: JSON file for storing member data.

test_app.py: Contains automated tests for the application.
test may fail cause not properly allinged 

## Working Mechanism
Data Storage: The application uses JSON files (books.json and members.json) to store data persistently. When the application starts, it reads these files to load existing data.

Routes: The application defines several routes for managing books and members:

# Using Postman would be better approach
```bash
/: Home page displaying counts of books and members.
/books/list: Lists all books.
/books/add: Adds a new book.
/books/edit/<id>: Edits an existing book.
/books/delete/<id>: Deletes a book.
/members/list: Lists all members.
/members/add: Adds a new member.
/members/edit/<id>: Edits an existing member.
/members/delete/<id>: Deletes a member.
/books/search: Searches for books.
/members/search: Searches for members.
```

HTML Templates: The application uses HTML templates to render the user interface. Each route corresponds to a specific template that displays the relevant data and forms for user interaction.

Automated Testing: The application includes a set of automated tests in test_app.py to ensure that all functionalities work as expected. You can run the tests using the following command:
test may fail cause not properly allinged 
```bash
python -m unittest tests/test_app.py
```

### 👨‍💻 About the Developer

**Aditya Tiwari**
- 💼 LinkedIn: [Aditya Tiwari](https://www.linkedin.com/in/aditya-tiwari-59b82927a/)
- 🐱 GitHub: [GitHub Profile](https://github.com/adi5423)
- 📧 Email: adii54ti23@gmail.com
- 🐦 Twitter: [@Adii5423](https://twitter.com/Adii5423)

Contributing
If you would like to contribute to this project, feel free to fork the repository and submit a pull request. Any contributions, suggestions, or improvements are welcome!
