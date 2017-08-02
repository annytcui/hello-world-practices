class BankAccount:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def __str__(self):
        msg = self.name + " account(No." + self.number + ") has a balance of " + str(self.balance) + "USD."
        return msg

    def makeDeposit(self, money):
        self.balance = self.balance + money

    def makeWithdrawal(self, money):
        self.balance = self.balance - money

class InterestAccount(BankAccount):
    def __init__(self, rate):
        BankAccount.__init__(self, "My", "1234567", 20000)
        self.rate = rate

    def addInterest(self, year):
        self.balance = self.balance * ((1 + self.rate) ** year)

myAccount = InterestAccount(0.05)
print myAccount
myAccount.addInterest(3)
print myAccount
