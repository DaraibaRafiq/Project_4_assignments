def main():
    user_input=int(input("Enter a year: "))
    if (user_input % 4 == 0 and user_input % 100 != 0) or (user_input % 400 == 0):
        print("This is a leap year.")
    else:   
        print("This is not a leap year.")
main()

