m = int(input("Which multiplication table would you like?"))
h = int(input("How high do you want to go?"))
print("Here's your table:")
for o in range(1,h + 1):
    print(m," x ",o," = ",m*o)
