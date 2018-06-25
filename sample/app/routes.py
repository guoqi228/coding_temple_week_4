from app import app
from flask import render_template, redirect, url_for

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Clay'}
    #return 'Hello Flask! This is a FLASK APP!'
    num = 2 + 2
    return render_template('index.html', user = user, num = num, title='Home Page')

@app.route('/posts')
def posts():
    posts = [
    'This is post 1',
    'This is post 2',
    'This is post 3',
    'Loopsing through the posts',
    'Flask!!!!!'
    ]
    return render_template('posts.html', title='Posts', posts = posts)

@app.route('/redirect')
def goaway():
    return redirect(url_for('index'))

#     '''
#
# <html>
#     <head>
#         <title> Home Page </title>
#     </head>
#     <body>
#         <h1> Hello ''' + user['username'] + ''' ! </h1>
#     </body>
# </html>
#
#
#     '''
