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
    return render_template("base.html", heading="Home Page", user=user_data)

# Login Route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if username in dummy_users and dummy_users[username]['password'] == password:
            session['user'] = username  # Store user in session
            return redirect(url_for("home"))
        else:
            return "Invalid credentials. Please try again.", 401
    return render_template("login.html", heading="Login")

# Logout Route
@app.route('/logout')
def logout():
    session.pop('user', None)  # Remove the user from session
    return redirect(url_for('home'))  # Redirect to the home page after logout

# Dashboard Route
@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        username = session['user']
        user_data = dummy_users[username]  # Get user data from session
        compliance_score = 75  # Example static score, replace with dynamic value
        last_audit_date = "15th December 2024"  # Example date
        return render_template("dashboard.html", user=user_data, compliance_score=compliance_score, last_audit_date=last_audit_date)
    else:
        # If the user is not logged in, display a login prompt or message
        return render_template("dashboard.html", user=None, compliance_score=None, last_audit_date=None, message="Please log in to view your dashboard.")

# Register Page
@app.route("/register")
def register():
    user_data = None
    if 'user' in session:
        username = session['user']
        user_data = dummy_users.get(username)  # Fetch the user data if logged in
    return render_template("register.html", heading="Register Page", user=user_data)

# Additional Pages (Documents, My Returns, etc.)
@app.route("/documents")
def documents():
    user_data = None
    if 'user' in session:
        username = session['user']
        user_data = dummy_users.get(username)
    return render_template("documents.html", heading="Documents Page", user=user_data)

# Settings Page
@app.route("/settings")
def settings():
    user_data = None
    if 'user' in session:
        username = session['user']
        user_data = dummy_users.get(username)
    return render_template("settings.html", heading="Settings Page", user=user_data)

# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", heading="404 - Page Not Found"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html", heading="500 - Internal Server Error"), 500

if __name__ == "__main__":
    app.run(debug=True)



