from database import engine, Base
from models import Client, SMSLog

Base.metadata.create_all(bind=engine)
print("Tables created successfully!")
