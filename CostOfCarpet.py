print "This program helps you calculate the total amount of carpet needed to cover your room and the cost of that carpet."
print "Let's get started!"
answer = raw_input("Is the shape of your room rectangular? ")
if answer == "yes" or answer == "Yes":
    length = float(raw_input("Please enter the length of your room in feet: "))
    width = float(raw_input("Please enter the width of your room in feet: "))
    CostPerSquareYard = float(raw_input("Please enter the cost per square yard of carpet in HKD: "))
    AreaSquareFeet = str(length * width)
    AreaSquareYard = str(length * width / 9.0)
    CostOfCarpet = str(CostPerSquareYard * length * width / 9.0)
    print "The total amount of carpet needed to cover your room is "+AreaSquareFeet+" square feet, or "+AreaSquareYard+" square yard."
    print "The cost of carpet is "+CostOfCarpet+" HKD."
else:
    print "Sorry, this program is not for you."
