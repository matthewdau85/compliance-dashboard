from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Home Route
@app.route("/")
def home():
    return render_template("home.html", heading="Home Page")

# Page Routes
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # Replace this with proper login logic
        if username == "admin" and password == "password":
            return redirect(url_for("home"))
        else:
            return "Invalid credentials. Please try again.", 401
    return render_template("login.html", heading="Login")

@app.route("/register")
def register():
    return render_template("register.html", heading="Register Page")

@app.route("/documents")
def documents():
    return render_template("documents.html", heading="Documents Page")

@app.route("/my_returns")
def my_returns():
    return render_template("my_returns.html", heading="My Returns Page")

@app.route("/notifications")
def notifications():
    return render_template("notifications.html", heading="Notifications Page")

@app.route("/payment_history")
def payment_history():
    return render_template("payment_history.html", heading="Payment History Page")

@app.route("/reports")
def reports():
    return render_template("reports.html", heading="Reports Page")

@app.route("/settings")
def settings():
    return render_template("settings.html", heading="Settings Page")

# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", heading="404 - Page Not Found"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html", heading="500 - Internal Server Error"), 500

if __name__ == "__main__":
    app.run(debug=True)

