from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime
from chatbot import get_bot_response

app = Flask(__name__)
app.secret_key = "student-project-secret-key"

DATABASE = "tickets.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def create_database():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            category TEXT NOT NULL,
            issue TEXT NOT NULL,
            status TEXT DEFAULT 'Open',
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    message = request.form.get("message", "").strip()
    if not message:
        reply = "Please type a message."
    else:
        reply = get_bot_response(message)
    return {"reply": reply}


@app.route("/ticket", methods=["GET", "POST"])
def ticket():
    if request.method == "POST":
        name = request.form["name"].strip()
        email = request.form["email"].strip()
        phone = request.form["phone"].strip()
        category = request.form["category"]
        issue = request.form["issue"].strip()

        if not name or not email or not phone or not issue:
            flash("Please fill all the required fields.")
            return redirect(url_for("ticket"))

        conn = get_db()
        cursor = conn.execute("""
            INSERT INTO tickets
            (name, email, phone, category, issue, status, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            name, email, phone, category, issue,
            "Open", datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))
        ticket_id = cursor.lastrowid
        conn.commit()
        conn.close()

        return render_template("success.html", ticket_id=ticket_id, name=name)

    return render_template("ticket.html")


@app.route("/tickets")
def tickets():
    conn = get_db()
    rows = conn.execute("SELECT * FROM tickets ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("tickets.html", tickets=rows)


@app.route("/update/<int:ticket_id>/<status>")
def update_status(ticket_id, status):
    allowed = ["Open", "In Progress", "Closed"]
    if status not in allowed:
        return "Invalid status", 400

    conn = get_db()
    conn.execute("UPDATE tickets SET status = ? WHERE id = ?", (status, ticket_id))
    conn.commit()
    conn.close()
    return redirect(url_for("tickets"))


if __name__ == "__main__":
    create_database()
    app.run(debug=True)
