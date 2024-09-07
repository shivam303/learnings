from flask import Flask , render_template,request

'''
It create an instance of flask class,
which will be your WSGI (Web Server Gateway Interface) Application

'''

app = Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to this flask tuts by Shivam Sachan"

@app.route("/index",methods = ['GET'])
def index():
    return render_template('index.html')

@app.route("/form",methods = ['GET','POST'])
def form():
    if request.method == 'POST':
        mail =  request.form['email']
        return f'Email-id is {mail}!' 
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug = True)