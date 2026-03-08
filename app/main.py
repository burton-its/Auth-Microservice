from fastapi import FastAPI, Depends, Response, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.db import get_db
from app.models import User
from app.schemas import RegisterIn, LoginIn
from app.core.security import hash_password, verify_password, create_access_token

app = FastAPI(title="Auth Service")

# Add PORTS to origins for handling cross-origin requests
origins = ['http://localhost:4000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# GET checks health of auth microservice
@app.get("/")
def read_root():
    return {"message": "FastAPI user Auth/login Auth/Register!"}


# POST adds newly registered user to DB
@app.post("/auth/register")
def register(payload:
        RegisterIn, db: Session = Depends(get_db)):
    try:
        existing = db.query(User).filter(User.email == payload.email).first()
        if existing:
            raise HTTPException(status_code=409, detail="Email already registered")

        user = User(
            email=payload.email,
            password_hash=hash_password(payload.password),
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return {"id": user.id, "email": user.email}
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=503, detail="Database unavailable")


# POST checks that user is registered and returns a token nested in
# http-only cookie for passing the token through requests from the browser
@app.post("/auth/login")
def login(payload: LoginIn, response: Response, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.email == payload.email).first()
        if not user or not verify_password(payload.password, user.password_hash):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        token = create_access_token(user_id=user.id, email=user.email)

        response.set_cookie(
            key="access_token",
            value=token,
            httponly=True,
            max_age=15 * 60
        )

        response.status_code = status.HTTP_200_OK
        return True

    except SQLAlchemyError:
        raise HTTPException(status_code=503, detail="Database unavailable")
