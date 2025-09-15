# Écrivez votre code ici !

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit_amount(self, deposit):
        deposit = float(input("How luch do you want to desposit ? "))
        print(f"current balance: {self.balance}")
        self.balance = self.balance + deposit
        print(f"deposit amount: {deposit} new balance: {self.balance}")
        return

    def withdraw_amount(self, withdraw):
        withdraw = float(input("How luch do you want to withdraw ? "))
        print(f"current balance: {self.balance}")
        self.balance = self.balance - withdraw
        print(f"deposit amount: {withdraw} new balance: {self.balance}")
        return

    def display_amount(self):
        print(f"the current balance is: {self.balance}")
        return


account = BankAccount("toto", 10000)
account.deposit_amount(500)
account.withdraw_amount(1000)
account.display_amount()


