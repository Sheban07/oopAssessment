class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"successful deposited: ${amount}")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Successful Withdrawn: ${amount}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance

account = BankAccount(10000)

# add money
account.deposit(500)

# Withdraw money
account.withdraw(200)
try:
    print(account.__balance)
except AttributeError:
    print("Direct access to balance is not allowed.")

print(f"Current Balance: ${account.get_balance()}")
