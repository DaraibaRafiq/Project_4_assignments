import random
print("The computer has thought of a number between (1,10) ! Try to guess it")
secret_number=random.randint(1,10)
try:
 while True:
  user_input=int(input("Make a guess between (1,10) ..."))
  if user_input == secret_number:
     print("You guessed it right!!")
     break
  elif user_input > secret_number:
     print("Think of something smaller....")
  elif user_input < secret_number:
     print("Think of something bigger....")
except ValueError :
     print ("Invalid input")
