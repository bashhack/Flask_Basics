from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name='Test User'):
    return 'Hello, {}'.format(name)

@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
def add(num1, num2):
    return render_template('add.html')

app.run(debug=True, port=8000, host='0.0.0.0')
