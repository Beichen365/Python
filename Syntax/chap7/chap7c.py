s = float(input("Size of tank :"))
p = float(input("Percent full :"))
k = float(input("km per liter :"))
dis = float(s*(p/100)*k)
print("You can go another ",dis," km")
print("The next gas station is 200 km away")
if dis < 200 :
    print("You cannot wait for the next station.")
elif dis >= 200 :
    print("You can wait for the next station.")

