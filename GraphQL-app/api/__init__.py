from flask import Flask,render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os



app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.getcwd()}/library.db"
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
db = SQLAlchemy(app)

@app.route('/')
def hello():
    return render_template('index.html')

