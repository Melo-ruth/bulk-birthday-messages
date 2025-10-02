import os
from dotenv import load_dotenv

load_dotenv()

print("DB_HOST=", os.getenv("DB_HOST"))
print("DB_USER=", os.getenv("DB_USER"))
print("DB_NAME=",os.getenv("DB_NAME"))

print("DB_PASSWORD =", os.getenv("DB_PASSWORD"))

# Print Africa's Talking vars
print("AT_USERNAME=", os.getenv("AT_USERNAME"))
print("AT_API_KEY=", os.getenv("AT_API_KEY"))