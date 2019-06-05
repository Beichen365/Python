price = float(input("What is the price ?"))
if price <= 10:
    print( "you got 10% discount")
    print("you need to pay",str(price*0.9)),"dollars"
elif price > 10:
    print("you got 20% discount")
    print("you need to pay",str(price*0.8),"dollars")


