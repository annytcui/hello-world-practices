print "Hi there! You have arrived at Gas Station A. The next station is 200km away."
print "How far can your car go from here? Can you wait until the next station?"
print "Let's find out!"

SizeOfTank = float(raw_input("How big is your gas tank, in liters? "))
PercentFull = float(raw_input("How full is your tank (in percent - for example, half full = 50)? "))
KmPerLiter = float(raw_input("How many km per liter does your car get? "))

KmCanGo = SizeOfTank * (PercentFull / 100) * KmPerLiter

print "Size of tank (liter): " + str(SizeOfTank)
print "Percent full: " + str(PercentFull)
print "km per liter: " + str(KmPerLiter)
print "You can go another "+ str(KmCanGo) + " km."
print "The next gas station is 200 km away."

if KmCanGo < 200:
    print "Get gas now!"
else:
    print "You can get gas now or wait until the next station!"
