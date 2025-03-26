minimum_height:int=50
def main():
    while True:
      user_input=float(input("Enter your height in inches: "))
      if user_input <= minimum_height:
        print("You are not tall enough to ride.")
        continue
      else:
        print("You are tall enough to ride.")
        break
main()

