class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"zakinyto {amount} denek, shas denek: {self.balance}")
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"snyato {amount} denek so schota, shas denek: {self.balance}")
        else:
            print("nehvatka sredstv")
account1 = BankAccount("1234567890", 1000)
account1.deposit(500)
account1.withdraw(200)
account2 = BankAccount("9876543210")
account2.deposit(1000)
account2.withdraw(1500)
