from flask import Flask, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index(): return '<h1>Hello, world!</h1>'

app.run('0.0.0.0', 80)
