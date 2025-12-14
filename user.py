from flask import render_template, redirect
from flask_login import login_required, current_user
from app import app
from db import get_db_connection

@app.route("/plan/<int:plan_id>")
@login_required
def plan_detail(plan_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True, buffered=True)

    cursor.execute("SELECT * FROM fitness_plans WHERE id=%s", (plan_id,))
    plan = cursor.fetchone()

    cursor.execute(
        "SELECT * FROM subscriptions WHERE user_id=%s AND plan_id=%s",
        (current_user.id, plan_id)
    )
    subscribed = cursor.fetchone()

    cursor.close()
    conn.close()

    return render_template("plan_detail.html", plan=plan, subscribed=subscribed)


@app.route("/subscribe/<int:plan_id>")
@login_required
def subscribe(plan_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO subscriptions (user_id, plan_id) VALUES (%s,%s)",
        (current_user.id, plan_id)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return redirect(f"/plan/{plan_id}")


@app.route("/feed")
@login_required
def feed():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True, buffered=True)
    cursor.execute("""
        SELECT fp.*
        FROM fitness_plans fp
        JOIN follows f ON fp.trainer_id = f.trainer_id
        WHERE f.user_id=%s
    """, (current_user.id,))
    plans = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("feed.html", plans=plans)

# Follow a trainer
@app.route("/follow/<int:trainer_id>")
@login_required
def follow(trainer_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Check if already following
    cursor.execute(
        "SELECT * FROM follows WHERE user_id=%s AND trainer_id=%s",
        (current_user.id, trainer_id)
    )
    exists = cursor.fetchone()

    if not exists:
        cursor.execute(
            "INSERT INTO follows (user_id, trainer_id) VALUES (%s,%s)",
            (current_user.id, trainer_id)
        )
        conn.commit()

    cursor.close()
    conn.close()
    return redirect(f"/trainer/{trainer_id}")


# Unfollow a trainer
@app.route("/unfollow/<int:trainer_id>")
@login_required
def unfollow(trainer_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM follows WHERE user_id=%s AND trainer_id=%s",
        (current_user.id, trainer_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(f"/trainer/{trainer_id}")