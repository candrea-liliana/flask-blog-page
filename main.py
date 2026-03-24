from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Lili Candrea',
        'title': 'First blog post',
        'content': 'First content post',
        'date_posted': 'Martie 21, 2026'
    },
    {
        'author': 'Anabelle',
        'title': 'Second blog post',
        'content': 'Second content post',
        'date_posted': 'Martie 22, 2026'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
