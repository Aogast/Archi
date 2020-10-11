from flask import Flask, url_for


app = Flask(__name__)


@app.route('/<name>')
def index(name):
    return 'http://127.0.0.1:8080/' + name


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')