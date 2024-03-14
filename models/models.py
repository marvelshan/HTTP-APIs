from models.database import db
from pydantic import BaseModel, field_validator


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)


class SignUpInput(BaseModel):
    username: str
    password: str

    @field_validator("username")
    def username_length(cls, v):
        if len(v) < 3 or len(v) > 32:
            raise ValueError("Username length must be between 3 and 32 characters")
        return v

    @field_validator("password")
    def password_length(cls, v):
        if len(v) < 8 or len(v) > 32:
            raise ValueError("Password length must be between 8 and 32 characters")
        return v

    @field_validator("password")
    def password_complexity(cls, v):
        if not any(char.isupper() for char in v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(char.islower() for char in v):
            raise ValueError("Password must contain at least one lowercase letter")
        if not any(char.isdigit() for char in v):
            raise ValueError("Password must contain at least one number")
        return v
