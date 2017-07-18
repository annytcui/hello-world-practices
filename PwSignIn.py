import easygui, random
from timeit import default_timer as timer
password = "Markanny2016"

easygui.msgbox("You need to type in a password to enter this program!")
choice = easygui.choicebox("To learn about the password, you need to answer 30 simple multiplication questions. If you get all of them right in 60 seconds, you will get the password. Are you ready?",
                  choices = ["Sounds interesting and YES!", "Ahhh, get out of here!"])
if choice == "Sounds interesting and YES!":
    easygui.msgbox("Let's get started!")
    Time1 = timer()
    rights = 0
    wrongs = 0
    number = 0
    while number < 30:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        answer = int(easygui.enterbox(str(a) + " X " + str(b) + " = "))
        if answer == a * b:
            rights = rights + 1
        else:
            wrongs = wrongs + 1
        number = number + 1

    Time2 = timer()
    Time = round((Time2 - Time1),2)
    
    if Time <= 60 and rights == 30:
        easygui.msgbox("Nice! You got all 30 questions right in 60 seconds! The password is " + password + ".")
        TypeIn = easygui.enterbox("Please type in the password: ")
        if TypeIn == password:
            easygui.msgbox("You are in!")
    else:
        easygui.msgbox("Sorry, you spend " + str(Time) + " seconds and got " + str(wrongs) + " question(s) wrong. You will not get the password.")
else:
    easygui.msgbox("Goodbye then!")







