from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def html():
    return "<html><H1> This is Flask baby </H1> </html>"

@app.route("/scenary")

def scenary():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)