import hashlib

# Stored username and hashed password
stored_username = "admin"

stored_password = "12345"
hashed_password = hashlib.sha256(stored_password.encode()).hexdigest()

# User input
username = input("Enter username: ")
password = input("Enter password: ")

# Hash user entered password
user_hash = hashlib.sha256(password.encode()).hexdigest()

# Authentication check
if username == stored_username and user_hash == hashed_password:
    print("Login successful")
else:
    print("Invalid username or password")