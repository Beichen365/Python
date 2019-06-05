def checkrepeat(no):
    x = ""
    for i in range(len(no)):
        for j in range(len(no)):
            if i != j and no[i] == no[j]:
                x = no[i]
        if x != "":
            break
    return x
print(checkrepeat([1,1, 2, 3, 3, 4, 5, 5]))

        
                   
