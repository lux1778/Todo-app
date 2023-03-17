from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

# todos = [{"task" : "Sample Todo", "done":False}]



@app.route("/")
def index():
    todos = Todo.query.all()
    return render_template("index.html", todos=todos)


@app.route("/add", methods=["POST"])
def add():
    todo = request.form['todo']
    new_todo = Todo(title=todo, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    # todos.append({"task": todo, "done" : False})
    return redirect(url_for("index"))

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    todo = Todo.query.filter_by(id=index).first()

    if request.method == 'POST':
        todo.title == request.form['todoedit']
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", todo=todo, index=index)


@app.route("/check/<int:index>")
def check(index):
    todo = Todo.query.filter_by(id=index).first()
    todo.complete = not todo.complete
    db.session.commit()
    # todos[index]['done'] = not todos[index]['done']
    return redirect(url_for("index"))

@app.route("/delete/<int:index>")
def delete(index):
    # del todos[index]
    todo = Todo.query.filter_by(id=index).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0")



