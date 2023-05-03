"""
Hook urls to html files in the templates directory.
"""
from flask import render_template, session, g
from app import app, database
import markdown


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    """
    Main landing page of aeryck.com.
    """
    db_conn = database.get_database()

    welcome_post = db_conn.execute(
        'SELECT p.id, created'
        ' FROM post p'
        ' WHERE title = "Welcome"'
    ).fetchone()
    session['post_id'] = welcome_post['id']

    return show_post_by_id(str(welcome_post['id']))



@app.route('/blog')
def blog():
    """
    Displays the titles of blog posts, with links to take the user to each
    post.
    """
    db_conn = database.get_database()
    posts = db_conn.execute(
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
    db_conn = database.get_database()
    post = db_conn.execute(
        'SELECT p.id, title, body, created'
        ' FROM post p'
        ' WHERE p.id = ?', (post_id),
    ).fetchone()
    g.id = post['id']
    title = post['title']

    older = db_conn.execute(
        'SELECT p.id'
        ' FROM post p'
        ' WHERE p.id = ?', (str(int(post_id) - 1),),
    ).fetchone()

    newer = db_conn.execute(
        'SELECT p.id'
        ' FROM post p'
        ' WHERE p.id = ?', (str(int(post_id) + 1),),
    ).fetchone()

    newest = db_conn.execute(
        'SELECT MAX(p.id)'
        ' FROM post p',
    ).fetchone()

    md_text = markdown.Markdown(extenstions=['fenced_code'])
    body = md_text.convert(post['body'])
    title = post['title']
    date = post['created']

    return render_template('index.html',
                           body=body,
                           title=title,
                           date=date,
                           older=older,
                           newer=newer,
                           newest=newest)


@app.route('/newest', methods=['GET'])
def show_newest_post():
    """
    Show the newest post in the database.

    This function retrieves the newest post in the database and stores its ID in
        the user's session. It then returns the result of the
        `show_post_by_id()` function, which displays the post with the given ID.

    Returns:
        render_template()

    Raises:
        None.

    """
    db_conn = database.get_database()
    newest_post = db_conn.execute(
        'SELECT p.id, created'
        ' FROM post p'
        ' WHERE p.id = (SELECT MAX(id) FROM post)',
    ).fetchone()
    session['post_id'] = newest_post['id']

    return show_post_by_id(str(newest_post['id']))



@app.route('/resume')
def show_resume():
    """
    Show Eric's current resume
    """
    return render_template('resume.html')
