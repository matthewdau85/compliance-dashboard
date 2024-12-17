from flask import Flask, render_template

app = Flask(__name__)

# Home Route
@app.route("/")
def home():
    return render_template("home.html")

# Page Routes
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/documents")
def documents():
    return render_template("documents.html")

@app.route("/my_returns")
def my_returns():
    return render_template("my_returns.html")

@app.route("/notifications")
def notifications():
    return render_template("notifications.html")

@app.route("/payment_history")
def payment_history():
    return render_template("payment_history.html")

@app.route("/reports")
def reports():
    return render_template("reports.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")

# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500

if __name__ == "__main__":
    app.run(debug=True)
