## Create a simple flask application

from flask import Flask,render_template

## create the flask app

app=Flask(__name__)

@app.route('/')
def home():
    return "<h2>Hello, World!</h2>"

@app.route('/welcome')
def welcome():
    return "Welcome to the Flask Tutorials"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/fail/<int:score>')
def fail(score):
    return "the person is failed and the  "+str(score)


if __name__=='__main__':
    app.run(debug=True)