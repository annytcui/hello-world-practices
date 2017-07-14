print "This program helps you add up your change."
print "Let's get started!"
Q = int(raw_input("How many quarters? "))
D = int(raw_input("How many dimes? "))
N = int(raw_input("How many nickels? "))
P = int(raw_input("How many pennies? "))
ChangeTotal = str(Q*0.25 + D*0.1 + N*0.05 + P*0.01)
print "The amount of change you have is "+ChangeTotal+" dollars."
