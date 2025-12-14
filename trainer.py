from flask import render_template, request, redirect
from flask_login import login_required, current_user
from app import app
from db import get_db_connection

@app.route("/trainer/dashboard")
@login_required
def trainer_dashboard():
    if current_user.role != "trainer":
        return redirect("/")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True, buffered=True)
    cursor.execute(
        "SELECT * FROM fitness_plans WHERE trainer_id=%s",
        (current_user.id,)
    )
    plans = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("trainer_dashboard.html", plans=plans)


@app.route("/trainer/create", methods=["GET", "POST"])
@login_required
def create_plan():
    if request.method == "POST":
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO fitness_plans (title,description,price,duration,trainer_id) VALUES (%s,%s,%s,%s,%s)",
            (
                request.form["title"],
                request.form["description"],
                request.form["price"],
                request.form["duration"],
                current_user.id
            )
        )
        conn.commit()
        cursor.close()
        conn.close()

        return redirect("/trainer/dashboard")

    return render_template("create_plan.html")

@app.route("/trainer/<int:trainer_id>")
@login_required
def trainer_profile(trainer_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True, buffered=True)

    # Trainer info
    cursor.execute("SELECT * FROM users WHERE id=%s AND role='trainer'", (trainer_id,))
    trainer = cursor.fetchone()

    # Trainer's plans
    cursor.execute("SELECT * FROM fitness_plans WHERE trainer_id=%s", (trainer_id,))
    plans = cursor.fetchall()

    # Check if current user is following this trainer
    cursor.execute(
        "SELECT * FROM follows WHERE user_id=%s AND trainer_id=%s",
        (current_user.id, trainer_id)
    )
    following = cursor.fetchone() is not None

    # Fetch list of plan_ids the current user has subscribed to
    cursor.execute(
        "SELECT plan_id FROM subscriptions WHERE user_id=%s",
        (current_user.id,)
    )
    subscriptions = cursor.fetchall()  # This will be a list of dicts like [{'plan_id': 1}, {'plan_id': 2}]
    subscribed_plan_ids={s['plan_id'] for s in subscriptions}
    cursor.close()
    conn.close()

    return render_template("trainer_profile.html", trainer=trainer, plans=plans, following=following, subscribed_plan_ids=subscribed_plan_ids)