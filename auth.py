from fastapi.security import (
    HTTPBearer
)
from passlib.context import CryptContext
from database import users_collection
from jose import jwt
from datetime import (
    datetime,
    timedelta
)
import os
from fastapi import (
    Depends,
    HTTPException
) 


SECRET_KEY = os.getenv(
    "SECRET_KEY"
)

ALGORITHM = "HS256"

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

oauth2_scheme = HTTPBearer()

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
        + timedelta(minutes=15)
    )

    payload = {
        "sub": str(user["id"]),
        "exp": expire
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

def get_current_user(
    credentials=Depends(oauth2_scheme)
):

    token = credentials.credentials

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        email = payload.get("sub")

        user_id = payload.get("sub")

        if user_id is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        user = users_collection.find_one(
            {"id": int(user_id)}
        )

        if user is None:
            raise HTTPException(
                status_code=401,
                detail="User not found"
            )

        return user

    except Exception as e:
        raise HTTPException(
            status_code=401,
            detail=str(e)
        )