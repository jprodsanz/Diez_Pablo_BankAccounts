class  BankAccount:
    accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print('negative funds: $100 Fee')
            self.balance -= 100
        return self

    def display_account_info(self):
        print(f'Balance: {self.balance}')
        return self
    
    def yield_interest(self):
        if self.balance > 0: 
            self.balance +=(self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

savings =  BankAccount(2000)
checking = BankAccount(750)

savings.deposit(30).deposit(50).withdraw(10).yield_interest().display_account_info()
savings.deposit(300).deposit(500).withdraw(100).yield_interest().display_account_info()

BankAccount.print_all_accounts() 
