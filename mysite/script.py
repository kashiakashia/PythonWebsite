# website made in python
from flask import Flask, render_template

# special variable that gets as __name__ python script's name
app = Flask(__name__)


@app.route('/')  # homepage
def home():
    return render_template("home.html")


@app.route('/about/')  # about page
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)
