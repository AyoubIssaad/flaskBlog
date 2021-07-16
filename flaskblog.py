from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    """Take me to route"""
    return "<h1>Hello, World!!</h1>"


@app.route("/about")
def about():
    """Take me to route"""
    return "<h1>About page</h1>"

if __name__ == '__main__':
    app.run(debug=True)
