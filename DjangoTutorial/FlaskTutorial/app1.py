from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1> This is first page </h1>"

@app.route('/contact')
def contact_me():
    return "<h1> This is Contact page </h1>"

@app.route('/')
def about_me():
    return "<h1> This is about page </h1>"
app.run(debug = True)

