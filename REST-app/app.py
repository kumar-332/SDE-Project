from api import app, db
from api.models import Post
from datetime import datetime
from flask import request, jsonify,render_template
import pandas as pd
import sqlite3

@app.route('/submit',methods=["GET","POST"])
def submit():
    if request.method == 'POST':
        current_date = datetime.today().date()
        book_title = request.form.get("title")
        desc = request.form.get("desc")
        author = request.form.get("author")
        genre = request.form.get("genre")
        new_post = Post(book_title=book_title, description=desc, created_at=current_date,author=author,genre=genre)
        db.session.add(new_post)
        db.session.commit()
    return render_template('form.html')


@app.route('/store')
def store():
    cnx = sqlite3.connect("library.db")
    df = pd.read_sql_query("select * from library", cnx)
    cnx.close()
    return render_template("store.html",tables=[df.to_html(classes=['table','table-striped'], header="true")])