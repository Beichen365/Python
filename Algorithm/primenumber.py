def isprime(no):
    a = 0
    for i in range(int(no - 2)):
        x = no % (i + 2)
        if x == 0:
            a += 1
    if a == 0:
        return True
    else:
        return False
def primepal(start, end):
    for i in range(start, end + 1):
        a = 0
        if isprime(i) == True:
            x = str(i)
            for j in range(len(x)):
                if x[j] != x[-j - 1]:
                    a += 1
            if a == 0:
                print(i)
primepal(100, 1000)
                

    
