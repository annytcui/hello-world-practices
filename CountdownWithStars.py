import time
print "This is a countdown timer!"
seconds = int(raw_input("How many seconds do you want to count down? "))
print "Nice choice. Let's get started!"

for i in range(seconds, 0, -1):
    print i,
    for j in range(i):
        print "*",
    print
print "Blast Off!"
        
