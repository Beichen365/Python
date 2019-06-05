import easygui
easygui.msgbox("This program converts Fahrenheit to Celsius")

tem = easygui.enterbox("Type in a temperature in Fahrenheit:")
b = float(tem)
c = (b-32)*5.0/9
d = str(c)
easygui.msgbox("That is " + d +  " degrees Celsius")

