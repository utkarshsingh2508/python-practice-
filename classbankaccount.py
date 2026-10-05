class BankAccount:
    def __init__(self,account_number,owner_name,balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposite(self, deposite_ammount):
        self.balance = self.balance + deposite_ammount
    
    def withdraw(self, withdraw_ammount):
        self.balance = self.balance - withdraw_ammount

    def check_balance(self):
        print(f"Total balance is {self.balance}")

p1 = BankAccount(9959958989,"Golu",50000)
p2 = BankAccount(9959644683,"Ravina",60000)
p3 = BankAccount(5665958989,"Bantu",80000)

p1.deposite(50000)
p1.withdraw(10000)
p2.check_balance()
print(p1.account_number,p1.owner_name,p1.balance)


    
        