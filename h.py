from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the SQLite database file
DATABASE_URL = 'sqlite:///registrations.db'

# Create the engine
engine = create_engine(DATABASE_URL)

# Define the base class for declarative models
Base = declarative_base()


# Define the Registration model
class Registration(Base):
    __tablename__ = 'registrations'

    id = Column(Integer, primary_key=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    university = Column(String(100), nullable=False)
    niveau_etude = Column(String(50), nullable=False)


# Create the table in the database
Base.metadata.create_all(engine)

print("Database and table created successfully!")
