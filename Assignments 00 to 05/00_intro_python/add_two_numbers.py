def sum ():
 try:
    num1=input("Enter your first number : ")
    num1=int(num1)
    num2=input("Enter your second number : ")
    num2=int(num2)
    total=num1+num2
    print(f"{num1} + {num2} = {total}")
 except ValueError:
    print("Invalid input! please enter number only")
sum()