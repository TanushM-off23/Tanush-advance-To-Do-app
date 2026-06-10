from flask import *
from app import db
from app.models.models import User

auth_bp = Blueprint("auth",__name__)




@auth_bp.route("/login", methods=["POST","GET"])
def login():
  if request.method=="POST":
    username = request.form.get("username")
    password = request.form.get("password")
    user=User.query.filter_by(username=username).first()
    if user and user.password==password:
      flash("You logged in Successfully")
      session["user"]=username
      return redirect(url_for("tasks.view_tasks")) 
    else:
      flash("Invalid credentials try again")
  return render_template("login.html")


@auth_bp.route("/logout")
def logout():
  session.pop("user", None)
  flash("You have been logged out!")
  return redirect(url_for("auth.login"))




    