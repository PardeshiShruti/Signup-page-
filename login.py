from sqlalchemy.orm import Session
import schemas
from fastapi import HTTPException
from passlib.context import CryptContext  # Used to hash passwords

# Initialize password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Verify the password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Login user
def loginuser(db: Session, email: str, password: str):
    # Check if the user exists in the database
    db_user = db.query(schemas.Blog).filter(schemas.Blog.email == email).first()
    
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    # Verify the provided password with the stored hashed password
    if not verify_password(password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    return {"message": "Logged in successfully"}1111111

