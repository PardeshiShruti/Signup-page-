#main.py

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import signup
import schemas
import database
import login

app = FastAPI()

# Create the database tables (if they don't exist)
schemas.Base.metadata.create_all(bind=database.engine)

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()  # Correctly reference SessionLocal
    try:
        yield db
    finally:
        db.close()

# Signup route
@app.post("/signup/")
def signup_route(email: str, password: str, confirm_password: str, db: Session = Depends(get_db)):
    return signup.signupuser(db=db, email=email, password=password, confirm_password=confirm_password)

@app.get("/login/{email}")
def loginuser(email: str, password: str, db: Session = Depends(get_db)):
    return login.loginuser(db=db, email=email, password=password) 
# @app.get("/user/{email}")
# def get_user(email: str):
#     # Since we are excluding the fake db, this method will return an error as we don't store users
#     return {"error": "No user persistence, data lost after request."}