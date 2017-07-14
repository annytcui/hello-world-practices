print "This program tells whether a number is odd or even. Let's get started!"
number = int(raw_input("Please enter an integer: "))
remainder = number % 2
if remainder == 0:
    print number, "is an even number!"
else:
    print number, "is an odd number!"
