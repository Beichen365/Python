def findsame(num1, num2):
    x = ""
    for i in range(len(num1)):
        for j in range(len(num2)):
            if num1[i] == num2[j]:
                x = x + str(num1[i]) + " "
    return x
print(findsame([1, 2, 5], [1, 3, 4,5]))
