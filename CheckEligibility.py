answer1 = raw_input("Are you a female? ")
if answer1 == "yes" or answer1 == "Yes":
    answer2 = int(raw_input("How old are you? "))
    if 10 <= answer2 <= 12:
        print "You are eligible to play on the team!"
    else:
        print "You are not eligible to play on the team!"
else:
    print "You are not eligible to play on the team!"
