def flipstr(str1):
    list1 = list(str1)
    list2 = []
    for i in range(len(list1)):
        list2.append(list1[-i - 1])
        str2 = "".join(list2)
    return str2
print(flipstr("123456abc"))
