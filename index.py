
from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    data = requests.get('https://us-central1-users-a5b92.cloudfunctions.net/api').content
    return render_template('about.html', about=json.loads(data)['data'])

if __name__ == '__main__':
    app.run(debug=True)