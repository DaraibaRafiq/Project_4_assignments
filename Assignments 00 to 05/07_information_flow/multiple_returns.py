def get_user_info():
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email = input("What is your email address?: ")
    return first_name, last_name, email

def main():
    user_data = get_user_info() 
    print(user_data)
main()
