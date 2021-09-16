from flask import Flask

application = Flask(__name__)


@application.route('/')
def hello_world():
    return 'Sup. Subscribe 2'


if __name__ == '__main__':
    application.run(debug=True, port=12100)
