from flask import Flask, request, redirect, jsonify, session, render_template, url_for
import os
from dotenv import load_dotenv
from flask_cors import CORS
import requests  # To make HTTP requests to your service-side app

load_dotenv()  # Load variables from .env file
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
AUTH_SERVICE_URL = os.getenv('AUTH_SERVICE_URL')  # URL of your authentication service

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'a_secret_key')  # Needed for session management
CORS(app)

@app.route('/')
def index():
    # Pass any necessary data to your front-end here
    return render_template('index.html', GOOGLE_API_KEY=GOOGLE_API_KEY)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Send login data to your authentication service
        response = requests.post(f'{AUTH_SERVICE_URL}/auth_api/login', json={
            'email': request.form['email'],
            'password': request.form['password']
        })

        if response.status_code == 200:
            # Login successful, handle session, redirection, etc.
            session['user'] = response.json()['email']  # Or any other user identifier
            return redirect(url_for('index'))
        else:
            # Login failed, handle accordingly
            return render_template('login.html', error="Invalid credentials")
    
    # For GET request, just display the login page
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Send registration data to your authentication service
        response = requests.post(f'{AUTH_SERVICE_URL}/aut_api/register', json={
            'email': request.form['email'],  #replace the string w this thing
            'password': request.form['password']
        })

        if response.status_code == 201:
            # Registration successful, you might want to auto-login the user or redirect to login page
            return redirect(url_for('login'))
        else:
            # Registration failed, handle accordingly
            return render_template('register.html', error="Registration failed")

    # For GET request, just display the registration page
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
