class BankAccount:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def __str__(self):
        msg = self.name + "'s account (No." + self.number + ") has a balance of " + str(self.balance) + "USD."
        return msg

    def makeDeposit(self, money):
        self.balance = self.balance + money

    def makeWithdrawal(self, money):
        self.balance = self.balance - money

print "Welcome to the self-help service of the Bank of Wonderland!"
name = str(raw_input("What is your full name? "))
myAccount = BankAccount(name, "1234567", 20000)
print myAccount

while 1:
    answer = str(raw_input("To deposit or to withdraw money (d/w)? Or type 'q' to quit. "))
    if answer == "d":
        money = float(raw_input("How much money would you like to deposit? "))
        myAccount.makeDeposit(money)
        print myAccount
    elif answer == "w":
        money = float(raw_input("How much money would you like to withdraw? "))
        myAccount.makeWithdrawal(money)
        print myAccount
    elif answer == "q":
        break
    else:
        print "Please type in 'd', 'w' or 'q'."
