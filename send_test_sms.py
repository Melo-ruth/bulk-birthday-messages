import africastalking

# Initialize Africa's Talking
username = "YOUR_SANDBOX_USERNAME"  # replace with your sandbox username
api_key = "atsk_d815740f9d4a9cbfeed6c98732bfb7a43e5ffc3f31987864ea94817dcdd034f94a91daf5"    # replace with your sandbox API key
africastalking.initialize(username, api_key)

sms = africastalking.SMS

# Test sending SMS
phone_number = "+2567XXXXXXXX"  # your sandbox number
message = "Hello Melissa! This is a test birthday message."

response = sms.send(message, [phone_number])
print(response)
