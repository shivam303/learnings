from flask import Flask 

'''
It create an instance of flask class,
which will be your WSGI (Web Server Gateway Interface) Application

'''

app = Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to this flask tuts by Shivam Sachan"

@app.route("/index")
def index():
    return "Welcome to the index page"

@app.route("/law")
def law():
    return "https://www.google.com/"

if __name__ == "__main__":
    app.run(debug = True)