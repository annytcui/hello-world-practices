import time
print "This is a countdown timer!"
seconds = int(raw_input("How many seconds do you want to count down? "))
print "Ok. Let's start!"

for i in range(seconds, 0, -1):
    print i
    time.sleep(1)
print "Blast Off!"
