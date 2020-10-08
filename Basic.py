from flask import Flask

app = Flask(__name__)

@app.route('/')
def First():
    return "Demo1"

@app.route('/name')
def name():
    return "My name is Sachin"
@app.route('/test/<name>')
def add(name):
    return "you have enetered "+name

if __name__ == '__main__':
    app.run(debug=True)
