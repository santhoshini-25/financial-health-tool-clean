from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

engine = create_engine(os.getenv('DATABASE_URL'))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class FinancialData(Base):
    __tablename__ = "financial_data"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    revenue = Column(String)  # JSON string for data
    expenses = Column(String)
    # Add more columns as needed
Base.metadata.create_all(bind=engine)