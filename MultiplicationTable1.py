import time
print "We can print multiplication tables for you!"
print "Choices range from 1 to 10."
time.sleep(2)

Num = int(raw_input("Which multiplication table would you like? (Enter an integer between 1 and 10) "))
if 1 <= Num <= 10:
    print "Good choice! Here is your table: "
    for i in range(1,11):
        print str(Num) + " X " + str(i) + " = " + str(i * Num)
else:
    print "Sorry, you have entered a number that is not between 1 and 10."
