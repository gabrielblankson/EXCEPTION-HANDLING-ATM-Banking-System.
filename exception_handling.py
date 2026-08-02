"""
ATM Banking System - Case Study
Week 8 - Exception Handling

Requirements:
- BankAccount class with deposit(), withdraw(), check_balance()
- Handle: negative deposit, insufficient funds, invalid withdrawal amount
- Custom exception: InsufficientFundsError
"""


class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the available balance."""
    pass


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative.")
        self.balance += amount
        print(f"Deposited GHS {amount:.2f}. New balance: GHS {self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw GHS {amount:.2f}. Available balance: GHS {self.balance:.2f}"
            )
        self.balance -= amount
        print(f"Withdrew GHS {amount:.2f}. New balance: GHS {self.balance:.2f}")

    def check_balance(self):
        print(f"Current balance: GHS {self.balance:.2f}")
        return self.balance


def main():
    account = BankAccount("Blankson Kwabena", balance=500)

    # Test: normal deposit
    try:
        account.deposit(600)
    except ValueError as e:
        print(f"Deposit error: {e}")
    finally:
        print("Deposit attempt processed.\n")

    # Test: negative deposit
    try:
        account.deposit(-50)
    except ValueError as e:
        print(f"Deposit error: {e}")
    finally:
        print("Deposit attempt processed.\n")

    # Test: withdrawal exceeding balance
    try:
        account.withdraw(1000)
    except InsufficientFundsError as e:
        print(f"Withdrawal error: {e}")
    except ValueError as e:
        print(f"Withdrawal error: {e}")
    finally:
        print("Withdrawal attempt processed.\n")

    # Test: invalid withdrawal amount
    try:
        account.withdraw(-20)
    except InsufficientFundsError as e:
        print(f"Withdrawal error: {e}")
    except ValueError as e:
        print(f"Withdrawal error: {e}")
    finally:
        print("Withdrawal attempt processed.\n")

    # Test: valid withdrawal
    try:
        account.withdraw(100)
    except InsufficientFundsError as e:
        print(f"Withdrawal error: {e}")
    except ValueError as e:
        print(f"Withdrawal error: {e}")
    finally:
        print("Withdrawal attempt processed.\n")

    account.check_balance()


if __name__ == "__main__":
    main()
