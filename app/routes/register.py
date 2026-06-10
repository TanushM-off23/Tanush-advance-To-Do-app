from app import db
from app.models.models import User
from flask import *
register_bp = Blueprint("register",__name__)

@register_bp.route("/register", methods=["GET","POST"])
def register():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Sorry Username Already taken")
            return redirect(url_for("register.register"))
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash("Account Made Succesfully!!!")
        return redirect(url_for("auth.login"))
    return render_template("register.html")


