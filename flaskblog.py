from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author':'Ayoub ISSAAD',
        'title':'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20,2018'
    },
    {
        'author':'Core Schafer',
        'title':'Blog Post 2',
        'content': 'second post',
        'date_posted': 'April 21,2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    """Take me to route"""
    return render_template('home.html', posts=posts, title='Home')


@app.route("/about")
def about():
    """Take me to route"""
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
