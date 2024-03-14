from flask import Blueprint, request, jsonify
from models.models import db, User
from sqlalchemy.exc import IntegrityError
import bcrypt
import os

authentication_bp = Blueprint("authentication_bp", __name__)


@authentication_bp.route("/signUp", methods=["POST"])
def signUp():
    try:
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

        return {"success": True}, 200
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"success": False, "reason": "Username already exists"}), 400
    except Exception as e:
        return jsonify({"success": False, "reason": str(e)}), 400
