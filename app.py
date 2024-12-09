from flask import Flask, render_template

app = Flask(__name__)

# Import routes
from routes import *

if __name__ == '__main__':
    app.run(debug=True)