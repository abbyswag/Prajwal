from flask import Flask
from flask import render_template
from flask_pymongo import PyMongo
from prajwal.server import serverFiles
 
# connecting mongodb database
app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'dbb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/dbb'
mongo = PyMongo(app)

# main routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/user')
def output():
    return render_template('user.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

# other routes
serverFiles(app)