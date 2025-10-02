from sqlalchemy import Column, String, Boolean, Date, Integer, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from database import Base
from datetime import datetime

class Client(Base):
    __tablename__ = "clients"
    
    id = Column(Integer, primary_key=True, index=True)
    national_id = Column(String(20), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    phone_number = Column(String(15), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    

class SMSLog(Base):
    __tablename__ = "sms_log"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    message = Column(String(255))
    status = Column(String(20))
   