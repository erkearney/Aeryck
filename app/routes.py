"""
Hook urls to html files in the templates directory.
"""
from flask import render_template, url_for, request, session, g
from app import app, database


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    """
    Main landing page of aeryck.com.
    """
    db = database.get_database()

    newest_post = db.execute(
        'SELECT p.id, created'
        ' FROM post p'
        ' WHERE created = (SELECT MAX(created) FROM post)'
    ).fetchone()
    session['post_id'] = newest_post['id']

    return show_post_by_id(str(newest_post['id']))



@app.route('/blog')
def blog():
    """
    Displays the titles of blog posts, with links to take the user to each
    post.
    """
    db = database.get_database()
    posts = db.execute(
        'SELECT * FROM post ORDER BY created DESC;'
    ).fetchall()
    return render_template('blog.html', posts=posts, title='Blog')


@app.route('/post:<string:post_id>', methods=['GET'])
def show_post_by_id(post_id):
    """
    Find and display a post by id number.

    TODO: Add an error page for when user manually navigates to a post that
    does not exist.
    """
    db = database.get_database()
    print(post_id)
    post = db.execute(
        'SELECT p.id, title, body, created'
        ' FROM post p'
        ' WHERE p.id = ?', (post_id),
    ).fetchone()
    g.id = post['id']
    title = post['title']

    older = db.execute(
        'SELECT p.id'
        ' FROM post p'
        ' WHERE p.id = ?', (str(int(post_id) - 1)),
    ).fetchone()

    newer = db.execute(
        'SELECT p.id'
        ' FROM post p'
        ' WHERE p.id = ?', (str(int(post_id) + 1)),
    ).fetchone()

    return render_template('index.html', post=post, title=title, older=older, newer=newer)


@app.route('/resume')
def show_resume():
    return render_template('resume.html')
