import easygui

easygui.msgbox("This program helps you add up your change.")
easygui.msgbox("Let's get started!")

Q = easygui.integerbox("How many quarters do you have?")
D = easygui.integerbox("How many dimes do you have?")
N = easygui.integerbox("How many nickels do you have?")
P = easygui.integerbox("How many pennies do you have?")

ChangeTotal = str(Q*0.25 + D*0.1 + N*0.05 + P*0.01)
easygui.msgbox("The amount of change you have is "+ChangeTotal+" dollars!")
