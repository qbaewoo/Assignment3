from flask import Flask, render_template
from flask import request
from flask.json import jsonify
import jwt
from flask_sqlalchemy import SQLAlchemy
import psycopg2


app = Flask(__name__,template_folder="my_templates")
app.config['SECRET_KEY'] = 'thisismyflasksecretkey'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234567@localhost:5432/user_table'
db = SQLAlchemy(app)
class User(db.Model):
    tablename = 'user_n'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    token = db.Column(db.String(120), unique=True, nullable=False)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login_ = request.form["login"]
        password = request.form["password"]
        user = User.query.filter_by(login=login_, password=password).first()
        if user is not None:
            user_token=jwt.encode({"login": login_, "password": password}, app.config['SECRET_KEY'], algorithm="HS256")
            user.token = user_token
            db.session.add(user)
            db.session.commit()
            return f"<h1>token: {user_token}</h1>"
        else:
            return f"<h1>Could not found a user with login: {login_}</h1>"
   
    return render_template("login.html")


@app.route("/protected",methods=["GET"])
def protected():
    s_token=request.args.get("token")
    jwt_token=jwt.decode(s_token,app.config['SECRET_KEY'],algorithms=["HS256"])
    if jwt_token:
        login_ = jwt_token.get("login")
        password = jwt_token.get("password")
        user = User.query.filter_by(login=login_, password=password).first()
        if user is not None:
            return "<h1>Hello, token which is provided is correct </h1>"
    return "<h1>Hello, Could not verify the token</h1>"


if name == '__main__':
    app.run(debug=True)
    db.create_all()