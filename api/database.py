from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv
# Load environment variables from the .env file
load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL")
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
dbname = os.getenv('DB_NAME')

DATABASE_URL = f"postgresql://{username}:{password}@{host}:{port}/{dbname}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base() 
Base.metadata.create_all(bind=engine)
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

