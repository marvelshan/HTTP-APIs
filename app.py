import os
from dotenv import load_dotenv
from flask import Flask, jsonify
from blueprints.authentication import authentication_bp
from models.database import db

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.errorhandler(404)
def page_not_found(error):
    error_message = {
        "message": "This page does not exist", "error": str(error)}
    return jsonify(error_message), 404


@app.errorhandler(Exception)
def handle_exception(error):
    error_message = {"message": "An error occurred", "error": str(error)}
    return jsonify(error_message), 500


app.register_blueprint(authentication_bp, url_prefix="/api")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
