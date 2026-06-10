from flask import *
from app import db
from  app.models.models import Task
from app.models.models import User
tasks_bp = Blueprint("tasks",__name__)

@tasks_bp.route("/")
def view_tasks():
   if "user" not in session:
      return redirect(url_for("auth.login"))
    
   tasks=Task.query.all()
   return render_template("tasks.html", tasks=tasks)

@tasks_bp.route("/add_task" , methods=["POST"])
def add_task():
   
   if "user" not in session:
      return redirect(url_for("auth.login")) 
   
   
   title=request.form.get("title")
   if title:
      new_task=Task(title=title , status="Pending")
      db.session.add(new_task)
      db.session.commit()
      flash("Task Added!!")

   return redirect(url_for("tasks.view_tasks"))


@tasks_bp.route("/toggle/<int:task_id>", methods=["GET"])
def toggle_status(task_id):
   if "user" not in session:
      return redirect(url_for("auth.login")) 
   task = db.session.get(Task, task_id)  
   if task:
    if task.status=="Pending":
      task.status="Working" 
    elif task.status=="Working":
      task.status="Done!"
    else:
      task.status="Pending"
   db.session.commit()
   return redirect(url_for("tasks.view_tasks"))



@tasks_bp.route("/clear" , methods=["POST"])
def clear_tasks():
   if "user" not in session:
      return redirect(url_for("auth.login")) 
  
  
   Task.query.delete()
   db.session.commit()
   flash("All Tasks Cleared!!!")
   return redirect(url_for("tasks.view_tasks"))

