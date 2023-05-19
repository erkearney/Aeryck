"""
Hook urls to html files in the templates directory.
"""
from typing import Optional, Tuple
from flask import render_template, session, g, Response, request, url_for
from werkzeug.exceptions import HTTPException
import markdown
import matplotlib.pyplot as plt
from app import app, database


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    """
    Main landing page of aeryck.com.
    """
    db_conn = database.get_database()

    welcome_post = db_conn.execute(
        'SELECT id, title'
        ' FROM post'
        ' WHERE title = "Welcome"'
    ).fetchone()
    session['post_id'] = welcome_post['id']

    return show_post(welcome_post['title'])


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


def get_post_title_by_id(post_id: int) -> Optional[str]:
    """
    Retrieve the post title for a given post ID.

    Query the database to get the post title corresponding to the given post ID.
    If the post ID does not exist, return None.

    Args:
        post_id: The ID of the post to retrieve the title for.

    Returns:
        The post title as a string, or None if the post ID does not exist.

    """
    db_conn = database.get_database()
    post = db_conn.execute(
        "SELECT title"
        " FROM post"
        " WHERE id = ?", (post_id,),
    ).fetchone()

    return post['title'] if post else None


def get_post(post_title):
    """
    Find a post by the posts' title.

    """
    db_conn = database.get_database()
    post = db_conn.execute(
        'SELECT id, title, body, created'
        ' FROM post'
        ' WHERE title = ?', (post_title,),
    ).fetchone()

    return post


@app.route("/post:<string:post_title>", methods=["GET"])
def show_post(post_title: str) -> Response:
    """
    Render a post from the database.

    Retrieve and display a post by its title. The post's ID is used to find
    the older, newer, and newest posts based on their ID values. The post
    content is converted from Markdown to HTML before being rendered.

    Args:
        post_title: The title of the post to display.

    Returns:
        A rendered template with the post content and navigation links.

    """
    db_conn = database.get_database()
    post = get_post(post_title)
    post_id = post["id"]
    g.id = post_id
    title = post['title']

    older_row = db_conn.execute(
        'SELECT MAX(id), title'
        ' FROM post'
        ' WHERE id < ?', (post_id,),
    ).fetchone()
    older_title = older_row["title"]

    newer_row = db_conn.execute(
        'SELECT MIN(id), title'
        ' FROM post'
        ' WHERE id > ?', (post_id,),
    ).fetchone()
    newer_title = newer_row["title"]

    newest_row = db_conn.execute(
        'SELECT MAX(id) AS id, title'
        ' FROM post',
    ).fetchone()
    newest_title = newest_row["title"] if newest_row["id"] != post_id else None

    md_text = markdown.Markdown(extenstions=['fenced_code'])
    body = md_text.convert(post['body'])
    title = post['title']
    date = post['created']

    return render_template('index.html',
                           body=body,
                           title=title,
                           date=date,
                           older_title=older_title,
                           newer_title=newer_title,
                           newest_title=newest_title)


@app.route('/latest')
def get_latest_post() -> str:
    """
    Get the title of the post with the largest ID value.

    Returns:
        str: The title of latest post from the database.
    """
    db_conn = database.get_database()
    latest_row = db_conn.execute(
        'SELECT MAX(id) AS id, title'
        ' FROM post',
    ).fetchone()
    latest_title = latest_row["title"]

    return show_post(latest_title)


@app.route('/resume')
def show_resume():
    """
    Show Eric's current resume
    """
    return render_template('resume.html')


@app.route('/pf-tool', methods=['GET', 'POST'])
def pf_tool():
    """
    PH
    """
    income = 0
    rent = 0
    food = 0
    utilities = 0
    income_earning_expenses = 0
    healthcare = 0
    minimum_debt_payments = 0
    message = 'Enter your basic budget information'

    if request.method == 'POST':
        try:
            income = float(request.form.get('income'))
            rent = float(request.form.get('rent'))
            food = float(request.form.get('food'))
            utilities = float(request.form.get('utilities'))
            income_earning_expenses = float(request.form.get('income_earning_expenses'))
            healthcare = float(request.form.get('healthcare'))
            minimum_debt_payments = float(request.form.get('minimum_debt_payments'))
        except ValueError:
            print('ValueError in GET')
            return render_template('pf-tool.html', img_url=None,
                                                   income=income,
                                                   rent=rent,
                                                   food=food,
                                                   utilities=utilities,
                                                   income_earning_expenses=income_earning_expenses,
                                                   healthcare=healthcare,
                                                   minimum_debt_payments=minimum_debt_payments,
                                                   message=message)

        total_essential_expenses = rent + food + utilities + income_earning_expenses + healthcare + minimum_debt_payments
        essentials_percent = 100 * total_essential_expenses / income if income != 0 else 100
        if essentials_percent > 100:
            message = f'Time to panic, your essential expenses account for {essentials_percent:.0f}% of your income, meaning this is unsustainable.'
        elif essentials_percent > 50:
            message = f'Your essential expenses account for {essentials_percent:.0f}% of your income. This is relatively high, you may need to explore options to either reduce your expenses by ${total_essential_expenses - income/2:.2f}, or increase your income to ${total_essential_expenses * 2:.2f}.'
        else:
            message = f'Excellent, your monthly essential expenses account for {essentials_percent:.0f}% of your income, which is below the recommended 50%.'
        budget_remaining = income - total_essential_expenses
        if income > 0 and budget_remaining >= 0:
            fig = plt.figure(figsize=(6,6))
            plt.pie([total_essential_expenses, budget_remaining], explode=(0.1, 0), shadow=True, startangle=90, colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'], labels=['essentials', 'remaining'], wedgeprops=dict(width=0.5), autopct='%1.1f%%')
            plt.title('Essential Expenses vs. Income', pad=20, color='#cccccc')
            plt.axis('equal')
            fig.patch.set_facecolor('#363535')

            pie_image = '/home/e/Documents/Aeryck/app/static/pie_chart.png'
            plt.savefig(pie_image)
            print(f'Saving to {pie_image}')
            plt.close()

            img_url = url_for('static', filename='pie_chart.png')

            return render_template('pf-tool.html', img_url=img_url,
                                                   income=income,
                                                   rent=rent,
                                                   food=food,
                                                   utilities=utilities,
                                                   income_earning_expenses=income_earning_expenses,
                                                   healthcare=healthcare,
                                                   minimum_debt_payments=minimum_debt_payments,
                                                   message=message)
        else:
            print(f'Users expenses: {total_essential_expenses} exceedes their income {income} :(')


    return render_template('pf-tool.html', img_url=None,
                                           income=income,
                                           rent=rent,
                                           food=food,
                                           utilities=utilities,
                                           income_earning_expenses=income_earning_expenses,
                                           healthcare=healthcare,
                                           minimum_debt_payments=minimum_debt_payments,
                                           message=message)


@app.errorhandler(404)
@app.errorhandler(500)
def handle_error(error: HTTPException) -> Tuple[Response, int]:
    """
    Handle 404 and 500 errors.

    Print the error and display an error page using the 'error.html' template.

    Args:
        error: The error object.

    Returns:
        A tuple containing the rendered error template and the error code.

    """
    print(f"ERROR: {error}")
    return render_template('error.html'), 404
