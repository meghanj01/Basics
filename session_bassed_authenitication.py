from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

# Hardcoded user data (for demonstration purposes)
users = {"megha": "megha", "user2": "password2"}

# Secret key for session management (change this to a strong, random value in production)
app.secret_key = "your-secret-key"


# Login route
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # Check if the username and password match
    if username in users and users[username] == password:
        # If the credentials are valid, set a session cookie (you can use more secure methods for session management)
        session["username"] = username
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Login failed"}), 401


# Protected route
@app.route("/protected", methods=["GET"])
def protected():
    # Check if the user is logged in by checking the session cookie
    if "username" in session:
        return (
            jsonify(
                {"message": "This is a protected endpoint", "user": session["username"]}
            ),
            200,
        )
    else:
        return jsonify({"message": "Unauthorized"}), 401


# Logout route
@app.route("/logout", methods=["GET"])
def logout():
    # Clear the session to log the user out
    session.pop("username", None)
    return jsonify({"message": "Logout successful"}), 200


if __name__ == "__main__":
    app.run(debug=True)
