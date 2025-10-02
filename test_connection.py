from database import SessionLocal

db = SessionLocal()
try:
    result = db.execute("SELECT 1").fetchone()
    print("Database connection successful:", result)
finally:
    db.close()
