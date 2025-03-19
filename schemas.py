#schemas.py
from sqlalchemy import Column, Integer, String
from database import Base

class Blog(Base):
    __tablename__ = "login"  # You might want to change this to something like 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)  # Ensure email is unique
    password = Column(String(255))  # Only store the password
