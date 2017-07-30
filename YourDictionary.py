print "Create your personal dictionary!"
MyDictionary = {}

a = 0
while a < 1:
    answer = str(raw_input("Add or look up a word (a/l)? Or type 'q' to quit the program. "))

    if answer == "a":
        key = str(raw_input("Type the word: "))
        value = str(raw_input("Type the definition: "))
        MyDictionary[key] = value
        print "Word added!"

    elif answer == "l":
        LookupKey = str(raw_input("Type the word: "))
        Checker = 0
        for key in MyDictionary.keys():
            if LookupKey == key:
                Checker = 1
                print key + ": " + MyDictionary[key]
        if Checker == 0:
            print "That word isn't in the dictionary yet!"
        
    elif answer == "q":
        print "You have quitted the program."
        break
