import random, easygui
score = 0
for Q_no in range(10):
    n1 = int(random.randint(1,10))
    n2 = int(random.randint(1,10))
    if random.randint(1,2) == 1:
        userAns = easygui.integerbox(str(n1) + " + " + str(n2) + " = ")
        if userAns == str(n1 + n2):
            easygui.msgbox("Correct!")
            score += 1
        else:
            easygui.msgbox("Wrong! The answer is ",n1 + n2)
    else:
        n1 = int(random.randint(1,20))
        n2 = int(random.randint(1,20))
        if n1 > n2:
            userAns = easygui.integerbox(str(n1) + " - " + str(n2) + " = ")
            if userAns == str(n1 - n2):
                easygui.msgbox("Correct!")
                score += 1
            else:
                easygui.msgbox("Wrong! The answer is ",n1 - n2)
        else:
            userAns = easygui.integerbox(str(n2) + " - " + str(n1) + " = ")
            if userAns == str(n2 - n1):
                easygui.msgbox("Correct!")
                score += 1
            else:
               easygui.msgbox ("Wrong! The answer is ",n2 - n1)
easygui.msgbox("Your final score is ",score," out of 10")
