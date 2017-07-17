import easygui

easygui.msgbox("This program helps you calculate the total amount of carpet needed to cover your room and the cost of that carpet.")
easygui.msgbox("Let's get started!")

answer = easygui.buttonbox("Is the shape of your room rectangular?",
                           choices = ["Yes", "No"])
if answer == "Yes":
    Length = float(easygui.enterbox("Nice! Please tell us the length of your room in feet: "))
    Width = float(easygui.enterbox("Then tell us the width of your room in feet: "))
    CostPerSquareFeet = float(easygui.enterbox("What is the cost of the carpet per square feet in HKD? "))
    Area = str(Length * Width)
    Cost = str(Length * Width * CostPerSquareFeet)
    easygui.msgbox("The total amount of carpet needed is " + Area + " square feet. The total cost is " + Cost + " HKD.")

else:
    easygui.msgbox("Sorry! This program is not for you =_=")
