import os
from dotenv import load_dotenv
from flask import Flask, jsonify
from flasgger import Swagger
from blueprints.authentication import authentication_bp
from models.database import db

load_dotenv()

app = Flask(__name__)
swagger = Swagger(app, template_file="docs/swagger.yml")

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.errorhandler(404)
def page_not_found(error):
    """
    Handle 404 errors by returning a custom JSON response.
    Parameters:
        - error: The error object provided by Flask.
    Returns:
        - A tuple containing a Flask jsonify response and the HTTP status code.
    """
    error_message = {
        "message": "This page does not exist", "error": str(error)}
    return jsonify(error_message), 404


@app.errorhandler(Exception)
def handle_exception(error):
    """
    Handle general exceptions by returning a custom JSON response.
    Parameters:
        - error: The error object provided by Flask.
    Returns:
        - On unexpected errors, returns a JSON object with an error message and a 500 status code.
    """
    error_message = {"message": "An error occurred", "error": str(error)}
    return jsonify(error_message), 500


app.register_blueprint(authentication_bp, url_prefix="/api")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
