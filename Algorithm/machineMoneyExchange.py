price = float(input("Price: "))
paid = float(input("Paid: "))
enough = False
while enough == False:
    if paid < price:
        print("Not enough money.")
        print("The cashier is very very very x 100 mad at you because your math is bad.")

        paid = float(input("Paid: "))
    else:
        enough = True
print("You should get:")
x = paid - price
money = [10000, 5000, 1000, 500, 100, 50, 10, 5, 1, 0.5, 0.2, 0.1, 0.05]
for looper in range(0,13):
    a = int(x / money[looper])
    x = x - money[looper] * a
    if a != 0:
        if money[looper] > 1:
            print(a," ",money[looper]," note(s).")
        else:
            if looper == 12:
                if x >= 0.03:
                    a = a + 1 
                    print(a," ",money[looper]," coin(s).")    
                else:
                    print(a," ",money[looper]," coin(s).")
            else:
                print(a," ",money[looper]," coin(s).")
    else:
        pass
if paid - price < 0.03:
    print("no change")
