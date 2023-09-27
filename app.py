from flask import Flask, jsonify, request, make_response, render_template
import jwt
import datetime
from functools import wraps

app = Flask("__name__")
app.config["SECRET_KEY"] = "wCWL8fo92XbiD-cD"
user = {"megha": "megha"}


@app.route("/login", methods=["POST"])
def login():
    auth = request.authorization
    breakpoint()
    if not auth or not auth.username or not auth.password:
        return jsonify(message="Authenitication failed"), 401

    user_name = auth.username
    password = auth.password
    if user_name in user and user[user_name] == password:
        token_payload = {
            "user_name": user_name,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
        }

        token = jwt.encode(token_payload, app.config["SECRET_KEY"], algorithm="HS256")
        return jsonify({"token": token})
    return jsonify(message="user authenitication failed"), 401


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get("token")
        if not token:
            return jsonify(message="token is missing"), 401
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms="HS256")
        except jwt.ExpiredSignatureError:
            return jsonify(message="Token has expired"), 401
        except jwt.InvalidTokenError:
            return jsonify(message="Invalid token"), 401

        return f(data, *args, **kwargs)

    return decorated


@app.route("/protected", methods=["GET"])
@token_required
def protected(data):
    return jsonify(message="Welcome to your profile"), 200


if __name__ == "__main__":
    app.run(debug=True)
