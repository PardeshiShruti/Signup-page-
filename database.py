from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection URL: 
# The format is: mysql+mysqlconnector://<username>:<password>@<host>:<port>/<dbname>
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:@localhost/basiclearn_db"

# Create the database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Declare the base class for model classes
Base = declarative_base()

# Create a sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 
