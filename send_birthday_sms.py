from database import SessionLocal
from models import Client
from datetime import date
from dotenv import load_dotenv
import os
import africastalking


#load envionment variables from 
load_dotenv()

# Initialize Africa's Talking
username = os.getenv("AT_USERNAME")
api_key = os.getenv("AT_API_KEY")
africastalking.initialize(username, api_key)
sms = africastalking.SMS

# Connect to DB
db = SessionLocal()

today = date.today()

# Find clients whose birthday is today and opted in
clients = db.query(Client).filter(
    Client.dob.month == today.month,
    Client.dob.day == today.day,
    Client.sms_opt_in == True
).all()

for client in clients:
    message = f"Happy Birthday, {client.first_name}! ForexBureau wishes you a great day. Reply STOP to unsubscribe."
    response = sms.send(message, [client.phone_e164])
    print(f"Sent to {client.first_name}: {response}")

db.close()
