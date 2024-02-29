import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config["SECRET_KEY"] = "idontknowwhythissecretkeymakesmycodeworkbutitdoessodonttouchit"

def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

def get_info(user_id):
    conn = get_db_connection()
    info = conn.execute("SELECT * FROM user_info WHERE id = ?",
                        (user_id,)).fetchone()
    conn.close()
    return info

@app.route("/")
def index():
    conn = get_db_connection()
    users = conn.execute("SELECT * FROM user_info").fetchall()
    conn.close()
    return render_template("index.html", users=users)

@app.route("/create/", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        name = request.form["name"]
        id = request.form["id"]
        score = request.form["score"]

        print(f"{name=}, {id=}, {score=}")
        if not name:
            flash("Name is required!")
        elif not id:
            flash("Id is required!")
        elif not score:
            flash("Score is required!")
        elif get_info(id):
            flash("Id is already taken!")
        elif "," in name:
            flash("Name must not contain commas! (sorry)")
        else:
            print("hello")
            conn = get_db_connection()
            conn.execute("INSERT INTO user_info (Name, Id, Score) VALUES (?, ?, ?)",
                         (name, id, score))
            conn.commit()
            conn.close()
            return redirect(url_for("index"))

    return render_template("create.html")

@app.route("/edit/<int:id>/", methods=("GET", "POST"))
def edit(id):
    info = get_info(id)

    if request.method == "POST":
        name = request.form["name"]
        score = request.form["score"]

        print(f"{name=}, {id=}, {score=}")
        if not name:
            flash("Name is required!")
        elif not score:
            flash("Score is required!")
        else:
            conn = get_db_connection()
            conn.execute("UPDATE user_info SET name = ?, score = ?"
                         " WHERE id = ?",
                         (name, score, id))
            conn.commit()
            conn.close()
            return redirect(url_for("index"))

    return render_template("edit.html", info=info)

@app.route("/delete/<int:id>", methods=("POST",))
def delete(id):
    print("thing")
    info = get_info(id)
    conn = get_db_connection()
    conn.execute("DELETE FROM user_info WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    flash(f"{info['name']} was successfully deleted!")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)