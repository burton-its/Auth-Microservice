# Validator Microservice

FastAPI JWT Token validation microservice for CS361.

## Contributors
- Sarah Van Hoose

## Getting Started
For the Testing program: You will need to download Node and run npm install to download the dependencies for this program.

For the main program, validator.py, ensure the following libraries are installed:

fastapi 
HTTPException
jose
CORSMiddleware
datetime
pydantic
requests
httpx

To run the main program continuously, from the root directory, enter the following in your terminal: uvicorn app.validator:app --reload --port 9000

(I chose port 9000 but you can configure it as you'd like)

Don't forget to add your local address to this code block if testing locally: origins = ['http://localhost:<PORT>']

This program needs to run in conjunction with AuthMicroservice - https://github.com/burton-its/Auth-Microservice - and Logout - https://github.com/burton-its/logout

## API Endpoints
- `GET /health` checks the health of the logout service endpoint
- `POST /get-token` retrieves raw token from logout service (specifically for revoke/logout procedures)
- `POST /validate/{jti}` retrieves from logout service whether token is active or has been revoked 
- `POST /revoke` calls logout service to revoke token
- `DELETE /cleanup` calls logout service to delete old tokens from blocklist
- `POST /validate-token` decides whether token is valid based on expiration and referencing the blocklist and returns info about token validity
