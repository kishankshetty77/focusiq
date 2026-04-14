from flask import Flask, render_template, request, redirect, url_for
from tasks import add_task, list_tasks, delete_task
from ai_advisor import get_ai_advice

app = Flask(__name__)

@app.route("/")
def index():
    tasks = list_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task_name = request.form.get("task")
    deadline = request.form.get("deadline")
    estimate = request.form.get("estimate")
    tags = request.form.get("tags")
    if task_name:
        add_task(task_name, deadline, estimate, tags)
    return redirect(url_for("index"))

@app.route("/delete/<int:number>")
def delete(number):
    delete_task(number)
    return redirect(url_for("index"))

@app.route("/advise")
def advise():
    advice = get_ai_advice()
    tasks = list_tasks()
    return render_template("index.html", tasks=tasks, advice=advice)

if __name__ == "__main__":
    app.run(debug=True)