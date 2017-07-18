print "Welcome to Markanny's!"
print "This program helps you figure out the suitale discount plan for you and the final price of your purchase."

OriginalPrice = float(raw_input("What is the original price of your purchase in dollar? "))
if OriginalPrice <= 10:
    FinalPrice = OriginalPrice * (1 - 0.1)
    print ("Wow, you can get a 10% off! The final price is only " + str(FinalPrice) + "!")
else:
    FinalPrice = OriginalPrice * (1 - 0.2)
    print ("Wow, you can get a 20% off! The final price is only " + str(FinalPrice) + "!")
