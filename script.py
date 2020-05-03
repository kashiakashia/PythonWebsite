# website made in python
from flask import Flask

app = Flask(__name__)


@app.route('/')  # home foler
def home():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)
