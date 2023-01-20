from flask import Flask, render_template, request

app = Flask(__name__)

posts = []

@app.route('/')
def hello_world():
    return render_template('home.html', posts=posts)

@app.route('/', methods=['POST'])
def post_comment():
    text = request.form['text']
    comment = {'content': text}
    posts.insert(0, comment)
    text = ''
    return render_template('home.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
