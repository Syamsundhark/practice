from src.practice1.util import *

my_account = BankAccount(1234567890, "rahul", balance=1000)

    # Deposit and withdraw
my_account.deposit(500)
my_account.withdraw(200)

    # Get current balance
current_balance = my_account.get_balance()
print(f"Current balance: ${current_balance}")