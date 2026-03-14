from datetime import datetime, timedelta, timezone
from jose import jwt
from passlib.context import CryptContext
import uuid

from app.core.config import JWT_SECRET, JWT_ALG, ACCESS_TOKEN_EXPIRE_SECONDS

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, password_hash: str) -> bool:
    return pwd_context.verify(password, password_hash)

def create_access_token(a_jti: str | None, user_id: int, email: str) -> str:
    now = datetime.now(timezone.utc)
    exp = now + timedelta(seconds=ACCESS_TOKEN_EXPIRE_SECONDS)

    my_jti = a_jti or str(uuid.uuid4())

    payload = {
        "sub": str(user_id),      
        "email": email,
        "jti": my_jti,
        "iat": int(now.timestamp()),
        "exp": int(exp.timestamp()),
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALG)