from api import app, db
from api.models import Post
from datetime import datetime
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify,render_template
from api.queries import listPosts_resolver
import pandas as pd

query = ObjectType("Query")
query.set_field("listPosts", listPosts_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, snake_case_fallback_resolvers
)
@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    print(data)
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code

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
    data = {
        'operationName': 'AllPosts',
        'variables': {},
        'query': 'query AllPosts {listPosts {success errors post {\
        id\
        book_title\
        author\
        genre }}}'
    }
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    df = pd.DataFrame(result['data']['listPosts']['post'])
    return render_template("store.html",tables=[df.to_html(classes=['table','table-striped'], header="true")])