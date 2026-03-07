from fastapi import FastAPI, Request, HTTPException, Response, status
from jose import JWTError, jwt
from datetime import datetime, timezone
from pydantic import BaseModel


app = FastAPI()


@app.post("/validate-token")
async def validator(request: Request, response: Response):
    my_token = await request.json()
    if my_token:
        payload = jwt.get_unverified_claims(my_token)
        exp_time = datetime.fromtimestamp(payload['exp'], timezone.utc)
        now_time = datetime.now(timezone.utc)

        if exp_time:
            # token is not expired
            if exp_time > now_time:
                # check if token is not already revoked by calling logout to check
                # make sure token was issued by login service
                response.status_code = status.HTTP_200_OK
                return True
        # add logic to call logout server revoke token API    
        raise HTTPException(status_code=422, detail="Invalid/expired token")

    else: 
        raise HTTPException(status_code=404, detail="No Token")
    # print(payload['exp'])n