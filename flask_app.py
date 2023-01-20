from flask import Flask, render_template, request

app = Flask(__name__)

# List of posts, everytime you submit a post gets added here
posts = []

@app.route('/')
def hello_world():
    return render_template('home.html', posts=posts)

# post request method, inserts the comment at the beginning of the posts list
# so the most recent comment shows up first
@app.route('/', methods=['POST'])
def post_comment():
    text = request.form['text']
    comment = {'content': text}
    posts.insert(0, comment)
    text = ''
    
    # Callback to the html template
    return render_template('home.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
