print("This program tells you if you are allowed to join the soccer team .")
age = float(input("What is your age ?"))
if 10 <= age <= 12:
    gen = input("What is your gender ?(M or F)")
    if gen == "F":
        print("You are allowed to join !")
    elif gen == "M":
        print("You are not allowed to join .")
elif age < 10 or age > 12:
    print("You are not allowed to join .")


