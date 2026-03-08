from fastapi import FastAPI, Request, HTTPException, Response, status
from jose import JWTError, jwt
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timezone
from pydantic import BaseModel
import requests
import httpx
from app.core.config import JWT_SECRET, JWT_ALG


app = FastAPI()

origins = ['http://localhost:4000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TokenRequest(BaseModel):
    token: str


@app.get("/health")
def health_check():
    logout_url = "http://localhost:5001/health"
    result = requests.get(logout_url).json
    return result


@app.post("/get-token")
def get_token(request: Request):
    token = request.cookies.get('access_token')
    return {"token": token}


@app.post("/validate/{jti}")
async def is_jti_revoked(jti: str):
    check_revoke_url = "http://localhost:5001/validate/{jti}"
    result = requests.get(check_revoke_url).json()
    return result


@app.post("/revoke")
async def revoke_jwt(body: TokenRequest):
    print(f"Received token: {body.token}") 
    revoke_url = "http://localhost:5001/revoke"
    async with httpx.AsyncClient() as client:
        result = await client.post(revoke_url, json={"token": body.token})
        return result.json()


@app.delete("/cleanup")
async def cleanup_blacklist():
    cleanup_url = "http://localhost:5001/cleanup"
    result = requests.delete(cleanup_url).json()
    return result


@app.post("/validate-token")
async def validator(body: TokenRequest, response: Response):
    my_token = body.token

    if my_token:
        payload = jwt.decode(my_token, JWT_SECRET, algorithms=[JWT_ALG])
        exp_time = datetime.fromtimestamp(payload['exp'], timezone.utc)
        now_time = datetime.now(timezone.utc)

        if not health_check():
            raise HTTPException(status_code=500, detail="Server-side error")

        # token is not expired
        if exp_time > now_time:
            my_jti = payload['jti']
            # check if token is already revoked by calling logout to check
            result = await is_jti_revoked(my_jti)
            if result['is_revoked']:
                raise HTTPException(status_code=401, detail="Unauthorized: Token revoked")
            response.status_code = status.HTTP_200_OK
            return True
        # call logout server revoke token API
        result = await revoke_jwt(my_token)
        raise HTTPException(status_code=401, detail="Unauthorized: Token revoked")
