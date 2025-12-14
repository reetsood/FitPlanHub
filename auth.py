from flask import render_template, request, redirect
from flask_login import login_user, logout_user, UserMixin, current_user
from app import app, login_manager
from db import get_db_connection
import bcrypt

class User(UserMixin):
    def __init__(self, id, name, role):
        self.id = id
        self.name = name
        self.role = role

@login_manager.user_loader
def load_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True, buffered=True)
    cursor.execute("SELECT * FROM users WHERE id=%s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user:
        return User(user["id"], user["name"], user["role"])
    return None


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        hashed = bcrypt.hashpw(
            request.form["password"].encode("utf-8"),
            bcrypt.gensalt()
        )

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (name, email, password, role) VALUES (%s,%s,%s,%s)",
            (
                request.form["name"],
                request.form["email"],
                hashed.decode("utf-8"),
                request.form["role"]
            )
        )
        conn.commit()
        cursor.close()
        conn.close()

        return redirect("/login")

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True, buffered=True)
        cursor.execute(
            "SELECT * FROM users WHERE email=%s",
            (request.form["email"],)
        )
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user and bcrypt.checkpw(
            request.form["password"].encode("utf-8"),
            user["password"].encode("utf-8")
        ):
            login_user(User(user["id"], user["name"], user["role"]))
            return redirect("/")

    return render_template("login.html")


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/login")




@app.route("/")
def landing():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True, buffered=True)

    if current_user.is_authenticated and current_user.role == "user":
        # fetch trainer_following for each plan
        cursor.execute("""
            SELECT fp.id, fp.title, fp.price, u.name AS trainer, u.id AS trainer_id,
                   (SELECT 1 FROM follows f WHERE f.user_id=%s AND f.trainer_id = u.id) AS trainer_following
            FROM fitness_plans fp
            JOIN users u ON fp.trainer_id = u.id
        """, (current_user.id,))
    else:
        # not logged in or trainer — default to 0
        cursor.execute("""
            SELECT fp.id, fp.title, fp.price, u.name AS trainer, u.id AS trainer_id,
                   0 AS trainer_following
            FROM fitness_plans fp
            JOIN users u ON fp.trainer_id = u.id
        """)

    plans = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("landing.html", plans=plans)
