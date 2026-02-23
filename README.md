# Auth Microservice

FastAPI authentication microservice for CS361.

## Contributors
- Corey Burton
- Samuel Vernick
- Sarah Van Hoose

## Communication Contract
- Our main method of communication will be our Discord Server.
- We are expected to respond within 48 hours.
- In case of upcoming deadlines and a team member is not reachable through Discord for 48 hours, the remaining team members will attempt to contact the team member through Microsoft Teams or university email. If the team member is still not reachable within 24 hours, the remaining team members will convene to decide next steps.
- Virtual meeting can be requested by any team member if they deem it necessary. Only one additional teammate needs to approve this meeting for it to procced.
- Work on a microservice should be reasonably split.

## requirements
- Python3.11+
- MySQL 8+
- venv

## project setup
``` 
create venv
pip install -r requirements.txt


in mysql (once running)
- host: '127.0.0.1'
- port: 3306
- db: authdb
- user: root
- pw : none 
mysql -u root < db.sql


then run main.py by ->

uvicorn app.main:app --reload --port 8000

-swagger is under http://127.0.0.1:8000/docs
```

## API Endpoints
- `GET /` health/welcome message
- `POST /auth/register` create a user account
- `POST /auth/login` verify credentials and return a token


## How to request data
- user sends JSON request and receives JSON response
- POST Request -> /auth/register
- Response -> "user created" - 200

## How to receive data
- user logs in and receives a JWT
- POST Request -> /auth/login
- Response -> JWT - 200

 ## Example Call
 - microservice exposes a REST API over HTTP
 - User communicates using json request bodies and receives a JWT

## UML diagram

![Auth Architecture Diagram](test.png)
