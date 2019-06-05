def fliplist(list1):
    list2 = []
    for i in range(len(list1)):
        list2.append(list1[-i - 1])
    return list2
print(fliplist([1, 2, 3]))
