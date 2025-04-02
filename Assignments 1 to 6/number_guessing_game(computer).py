import random
print("Think of a number between 1 to 10")
user_input=int(input("Enter your secret number (computer will guess it) "))

computer_number=random.randint(1,10)
print(f"Computer's first guess is {computer_number}")

while True :
  feedback=input("Is this guess correct ? (high , low  or correct) ")
  if feedback == "correct":
     print("Yayy!! The computer guessed it right....")
     break
  elif feedback == "low":
     print("Computer's guess is low...")
  elif feedback == "high" :
     print("Computer's guess is high...")
  else :
     print("Invalid input! Please type only high, low or correct")
     continue
  computer_number=random.randint(1,10)
  print(f"Computer's new guess is {computer_number}")