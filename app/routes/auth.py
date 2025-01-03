from flask import Blueprint, render_template, request, redirect, url_for, session
from ..models import User
from ..extensions import db


bp = Blueprint('auth', __name__)

@bp.route("/")
def home():
    if "username" in session:
        return redirect(url_for('dashboard.dashboard'))
    return render_template('index.html')


@bp.route("/login", methods=["POST"])
def login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        session['username']= username

        return redirect(url_for('dashboard.dashboard'))
    elif not User:
        return render_template('index.html', error="User does not exist, please register an account")
    else:
        return render_template('index.html', error="Username or password does not match")


@bp.route("/register", methods=["POST"])
def register():
    username = request.form['username']
    password  = request.form['password']
    email = request.form['email']
    school = request.form['school']
    department = request.form['department']
    about = request.form.get('about', '')

#checks
    user = User.query.filter_by(username=username).first()
    if user:
        return render_template("index.html", error="User already exists, login instead")
    
    elif User.query.filter_by(email=email).first():
        return render_template("index.html", error="Email already registered, try logging in")
    else:
        new_user = User(username=username, email=email, school=school, department=department, about=about)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        session['username'] = username
        return redirect(url_for('dashboard.dashboard'))
    




@bp.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('auth.home'))



