from flask import Blueprint, render_template, session, redirect, url_for
from ..models import User

bp = Blueprint('dashboard', __name__)

@bp.route("/dashboard")
def dashboard():
    if "username" in session:
        user = User.query.filter_by(username=session["username"]).first()
        return render_template("dashboard.html", user=user)
    return redirect(url_for('home'))