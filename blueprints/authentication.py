import os
import bcrypt
from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from pydantic import ValidationError
from models.models import db, User, Sign_up_input, Sign_in_input


authentication_bp = Blueprint("authentication_bp", __name__)


@authentication_bp.route("/signUp", methods=["POST"])
def sign_up():
    """
    Register a new user.

    This endpoint receives a JSON request containing the user's username and password.
    The password is hashed using bcrypt before being stored in the database.

    Returns:
        - A JSON response indicating success or failure.
            - If successful, returns {"success": True} and status code 201.
            - If there are validation errors, returns {"success": False, "reason": [error messages]} and status code 400.
            - If a user with the same username already exists, returns {"success": False, "reason": "Username already exists"} and status code 409.
    """
    try:
        Sign_up_input(**request.json)
        data = request.json
        username = data.get("username")
        password = data.get("password")

        salt_rounds = int(os.getenv("SALT_ROUND"))
        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"), bcrypt.gensalt(rounds=salt_rounds)
        )
        new_user = User(username=username, password_hash=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        return jsonify(success=True), 201
    except ValidationError as e:
        error_messages = []
        for error in e.errors():
            error_messages.append(error["msg"])
        return jsonify(success=False, reason=error_messages), 400
    except IntegrityError:
        db.session.rollback()
        error_message = {"success": False, "reason": "Username already exists"}
        return jsonify(error_message), 409


@authentication_bp.route("/signIn", methods=["POST"])
def sign_in():
    """
    Sign in an existing user.

    This endpoint receives a JSON request containing the user's username and password.
    It checks if the username exists in the database and if the provided password matches the hashed password.

    Returns:
        - A JSON response indicating success or failure.
            - If successful, returns {"success": True} and status code 200.
            - If the username or password is invalid, returns {"success": False, "reason": "Invalid password"} and status code 401.
            - If the user does not exist, returns {"success": False, "reason": "User not found"} and status code 404.
        - If there are validation errors, returns {"success": False, "reason": [error messages]} and status code 400.
    """
    try:
        Sign_in_input(**request.json)
        data = request.json
        username = data.get("username")
        password = data.get("password")

        user = User.query.filter_by(username=username).first()
        if user:
            if bcrypt.checkpw(
                password.encode("utf-8"), user.password_hash.encode("utf-8")
            ):
                return jsonify(success=True), 200
            else:
                return jsonify(success=False, reason="Invalid password"), 401
        else:
            return jsonify(success=False, reason="User not found"), 404

    except ValidationError as e:
        error_messages = [error["msg"] for error in e.errors()]
        return jsonify(success=False, reason=error_messages), 400
