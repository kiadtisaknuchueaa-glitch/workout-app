from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
from flask import request

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        pw = request.form["password"]

        if user == "admin" and pw == "1234":
            return "✅ เข้าสำเร็จ!"
        else:
            return "❌ ผิด"

    return render_template("login.html")
@app.route("/workout")
def workout():
    return "Push-up 20 | Squat 30 | Plank 60 วิ"
