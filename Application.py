from flask import Flask
from flask import render_template
from flask_pymongo import PyMongo
from server import serverFiles
 
app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'dbb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/dbb'
mongo = PyMongo(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

serverFiles(app)