from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Space is the new world test!!!'
