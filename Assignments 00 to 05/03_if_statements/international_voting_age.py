PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

def main():
 user_input=int(input("Enter your age: "))
 if user_input >= PETURKSBOUIPO_AGE:
    print("You are old enough to vote in Peturksbouipo.")
 else:
    print("You are not old enough to vote in Peturksbouipo.")
 if user_input >= STANLAU_AGE:
    print("You are old enough to vote in Stanlau.")
 else:
    print("You are not old enough to vote in Stanlau.")
 if user_input >= MAYENGUA_AGE:
    print("You are old enough to vote in Mayengua.")
 else:
    print("You are not old enough to vote in Mayengua.")
main()