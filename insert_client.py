from database import SessionLocal
from models import Client
from datetime import date

db = SessionLocal()

# Create a test client
new_client = Client(
    first_name="Melissa",
    last_name="Aine",
    national_id="12345678",
    phone_e164="+2567XXXXXXXX",  # replace with a sandbox number from Africa's Talking
    dob=date(2025, 10, 2),        # replace with today’s date to test birthday logic
    sms_opt_in=True
)

db.add(new_client)
db.commit()
db.close()

print("Test client added!")
