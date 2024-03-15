import os
import bcrypt
from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from pydantic import ValidationError
from models.models import db, User, Sign_up_input, Sign_in_input


authentication_bp = Blueprint("authentication_bp", __name__)


@authentication_bp.route("/signUp", methods=["POST"])
def sign_up():
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
        return jsonify(error_message), 400


@authentication_bp.route("/signIn", methods=["POST"])
def sign_in():
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
