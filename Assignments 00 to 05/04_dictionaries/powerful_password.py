from hashlib import sha256

def hash_password(password):
    # Converts the password into a hashed version using sha256
    return sha256(password.encode()).hexdigest()

def login(email, stored_logins, password_to_check):
    # Hash the password user entered
    hashed_password = hash_password(password_to_check)
    
    # Check if the email exists and if the hashed passwords match
    if email in stored_logins and stored_logins[email] == hashed_password:
        return True
    else:
        return False

def main():
    # A dictionary storing emails and their hashed passwords
    stored_logins = {
        "example@gmail.com": hash_password("password"),
        "code_in_placer@cip.org": hash_password("Karel"),
        "student@stanford.edu": hash_password("123!456?789")
    }
    
    # Testing the login system
    print(login("example@gmail.com", stored_logins, "word"))          # False (wrong password)
    print(login("example@gmail.com", stored_logins, "password"))       # True (correct password)
    print(login("code_in_placer@cip.org", stored_logins, "Karel"))     # True (correct password)
    print(login("code_in_placer@cip.org", stored_logins, "karel"))     # False (case-sensitive)
    print(login("student@stanford.edu", stored_logins, "password"))    # False (wrong password)
    print(login("student@stanford.edu", stored_logins, "123!456?789")) # True (correct password)

main()
