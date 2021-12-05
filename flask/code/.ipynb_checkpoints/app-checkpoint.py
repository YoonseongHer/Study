from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def home():
    res = requests.get('http://58.181.51.162:5000/bye')
    return 'Hello, World!' + res.text

@app.route('/bye')
def home_():
    return 'bye'

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)