from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # For session management

# Simulated dummy database for Matthew Donovan
dummy_users = {
    'matthew': {'password': 'password', 'name': 'Matthew Donovan', 'age': 39, 'email': 'matthew.donovan@alumni.griffithuni.edu.au'},
}

# Home Route
@app.route("/")
def home():
    user_data = None
    if 'user' in session:
        username = session['user']
        user_data = dummy_users.get(username)  # Fetch the user data if logged in
    return render_template("home.html", heading="Home Page", user=user_data, dummy_users=dummy_users)

# Login Route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if username in dummy_users and dummy_users[username]['password'] == password:
            session['user'] = username  # Store user in session
            return redirect(url_for("dashboard"))
        else:
            return "Invalid credentials. Please try again.", 401
    return render_template("login.html", heading="Login")

# Dashboard Route
@app.route("/dashboard")
def dashboard():
    if 'user' in session:
        username = session['user']
        user_data = dummy_users[username]  # Fetch user data based on session
        return render_template("dashboard.html", user=user_data, dummy_users=dummy_users)  # Pass user data to template
    else:
        return redirect(url_for('login'))  # If not logged in, redirect to login

# Register Page
@app.route("/register")
def register():
    user_data = None
    if 'user' in session:
        username = session['user']
        user_data = dummy_users.get(username)  # Fetch the user data if logged in
    return render_template("register.html", heading="Register Page", dummy_users=dummy_users, user=user_data)

# Documents Page
@app.route("/documents")
def documents():
    user_data = None
    if 'user' in session:
        username = session['user']
        user_data = dummy_users.get(username)  # Fetch the user data if logged in
    return render_template("documents.html", heading="Documents Page", dummy_users=dummy_users, user=user_data)

# My Returns Page
@app.route("/my_returns")
def my_returns():
    user_data = None
    if 'user' in session:
        username = session['user']
        user_data = dummy_users.get(username)  # Fetch the user data if logged in
    return render_template("my_returns.html", heading="My Returns Page", dummy_users=dummy_users, user=user_data)

# Notifications Page
@app.route("/notifications")
def notifications():
    user_data = None
    if 'user' in session:
        username = session['user']
        user_data = dummy_users.get(username)  # Fetch the user data if logged in
    return render_template("notifications.html", heading="Notifications Page", dummy_users=dummy_users, user=user_data)

# Payment History Page
@app.route("/payment_history")
def payment_history():
    user_data = None
    if 'user' in session:
        username = session['user']
        user_data = dummy_users.get(username)  # Fetch the user data if logged in
    return render_template("payment_history.html", heading="Payment History Page", dummy_users=dummy_users, user=user_data)

# Reports Page
@app.route("/reports")
def reports():
    user_data = None
    if 'user' in session:
        username = session['user']
        user_data = dummy_users.get(username)  # Fetch the user data if logged in
    return render_template("reports.html", heading="Reports Page", dummy_users=dummy_users, user=user_data)

# Settings Page
@app.route("/settings")
def settings():
    user_data = None
    if 'user' in session:
        username = session['user']
        user_data = dummy_users.get(username)  # Fetch the user data if logged in
    return render_template("settings.html", heading="Settings Page", dummy_users=dummy_users, user=user_data)

# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", heading="404 - Page Not Found"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html", heading="500 - Internal Server Error"), 500

# Logout Route
@app.route('/logout')
def logout():
    session.pop('user', None)  # Remove user from session
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)


