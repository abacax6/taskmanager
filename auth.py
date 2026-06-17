from passlib.context import CryptContext
from database import users_collection
from jose import jwt
from datetime import (
    datetime,
    timedelta
)
import os

SECRET_KEY = os.getenv(
    "SECRET_KEY"
)

ALGORITHM = "HS256"

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(password, hashed):
    return pwd_context.verify(
        password,
        hashed
    )

def authenticate_user(
    email: str,
    password: str
):

    user = users_collection.find_one(
        {"email": email}
    )

    if user is None:
        raise ValueError(
            "Invalid credentials"
        )

    if not verify_password(
        password,
        user["password"]
    ):
        raise ValueError(
            "Invalid credentials"
        )

    return user

def create_access_token(
    user
):

    expire = (
        datetime.now()
        + timedelta(hours=1)
    )

    payload = {
        "sub": user["email"],
        "exp": expire
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )