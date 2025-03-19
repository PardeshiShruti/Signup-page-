#signup.py
from sqlalchemy.orm import Session
import schemas
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from passlib.context import CryptContext  # Used to hash passwords

# Initialize password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hash the password
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Create a new user (signup)
def signupuser(db: Session, email: str, password: str, confirm_password: str):
    # Check if the passwords match
    if password != confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")
    
    # Check if the email already exists in the database
    db_user = db.query(schemas.Blog).filter(schemas.Blog.email == email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Hash the password before storing it
    hashed_password = hash_password(password)
    
    # Create a new user record
    db_user = schemas.Blog(email=email, password=hashed_password)
    db.add(db_user)
    try:
        db.commit()
        db.refresh(db_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email already registered")
    
    return db_user




# # Get a blog by its ID
# def login(db: Session, email: str, password: str):
#     # Query the database for the blog or user by email and password
#     blog = db.query(schemas.Blog).filter(schemas.Blog.email == email, schemas.Blog.password == password).first()

#     # If no blog found with the given email and password, raise an exception
#     if not blog:
#         raise HTTPException(status_code=404, detail="Blog not found or incorrect credentials")

#     # Return the blog details or a relevant response
#     return blog
