from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# ✅ สร้าง database
def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# 🏠 หน้าแรก
@app.route("/")
def home():
    return render_template("index.html")

# 🔐 สมัคร
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = request.form["username"]
        pw = request.form["password"]

        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user, pw))
        conn.commit()
        conn.close()

        return "✅ สมัครสำเร็จ!"

    return render_template("register.html")

# 🔑 login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        pw = request.form["password"]

        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (user, pw))
        result = c.fetchone()
        conn.close()

        if result:
            return redirect("/workout")
        else:
            return "❌ ผิด"

    return render_template("login.html")

# 💪 workout
@app.route("/workout")
def workout():
    return "🔥 โปรแกรม: Push-up 20 | Squat 30 | Plank 60 วิ"

# 🌍 run
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
