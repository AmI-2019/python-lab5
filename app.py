from flask import Flask, render_template,redirect, url_for,request
import db_interaction
app = Flask(__name__)


@app.route('/')
def index_redirect():
    return redirect(url_for("index"))


@app.route('/index')
def index():
    tasks = db_interaction.get_tasks()
    return render_template("index.html", tasks = tasks)


@app.route('/insert_task', methods=["post"])
def insert_task():
    todo = request.form["todo"]
    urgent = request.form.get("todo", False)
    db_interaction.insert_task(todo,urgent)
    return redirect(url_for("index"))


@app.route('/delete_task/<int:id>')
def delete_task(id):
    db_interaction.remove_task_by_id(id)
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run()
