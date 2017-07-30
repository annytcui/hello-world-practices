def countChange(quarters, dimes, nickels, pennies):
    total = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    return total

List = []
for change in ["quarters", "dimes", "nickels", "pennies"]:
    change = int(raw_input("How many " + change + " do you have? "))
    List.append(change)

quarters = List[0]
dimes = List[1]
nickels = List[2]
pennies = List[3]

total = countChange(quarters, dimes, nickels, pennies)
print "The change you have is " + str(total) + " USD.56"
