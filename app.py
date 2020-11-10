from flask import Flask, render_template
from pyrebase import pyrebase

config = {
  "apiKey": "AIzaSyBmkAKKz6eqzKrtNp4uG1pOlHmGcuqj804",
  "authDomain": "royal-earthmovers.firebaseapp.com",
  "databaseURL": "https://royal-earthmovers.firebaseio.com",
  "projectId": "royal-earthmovers",
  "storageBucket": "royal-earthmovers.appspot.com",
  "messagingSenderId": "149139328882",
  "appId": "1:149139328882:web:406edce340a03891e4d7eb",
  "measurementId": "G-FPVMM1SWY4"
}


app = Flask(__name__)

#index route
@app.route('/')
def index():
     return render_template('login.html')


#about page
@app.route('/invoice')
def about():
    return render_template('basic_elements.html')

#service
@app.route('/dashboard')
def dashboard():
    return render_template('index.html')

#clients
@app.route('/client')
def client():
   return render_template('client.html')

#careers
@app.route('/career')
def career():
   return render_template('career.html')

#contact
@app.route('/contact')
def contact():
   return render_template('contact.html')

if __name__ == '__main__':
     app.run(debug=True)


