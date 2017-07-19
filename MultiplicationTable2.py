import time
print "We can print multiplication tables for you!"
print "Choices range from 1 to 100."
time.sleep(2)
Num1 = int(raw_input("Which multiplication table would you like? (Enter an integer between 1 and 100) "))
if 1 <= Num1 <= 100:
    Num2 = int(raw_input("How high do you want to go? (Enter an integer between 1 and 100) "))
    if 1 <= Num2 <= 100:
        print "Good choice! Here is your table: "
        time.sleep(1)
        i = 1
        while i <= Num2:
            print str(Num1) + " X " + str(i) + " = " + str(Num1 * i)
            i = i + 1
    else:
        print "Sorry, the number you entered is not between 1 and 100."
else:
    print "Sorry, the number you entered is not between 1 and 100."
