from flask import Flask

application = Flask(__name__)
app = application


@app.route('/')
def hello_world():
    return 'Sup. Subscribe 2'


if __name__ == '__main__':
    app.run(debug=True, port=12100)
