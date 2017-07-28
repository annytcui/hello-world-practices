import time
print "Create your personal dictionary!"
MyDictionary = {}

key = str(raw_input("Type the word: "))
value = str(raw_input("Type the definition: "))
MyDictionary[key] = value
print "Word added!"

time.sleep(2)

answer = str(raw_input("Add or look up a word (a/l)? "))
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
        
else:
    print "Sorry, we cannot help you. You need to type in either 'a' or 'l'."
