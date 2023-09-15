class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      return f"Deposited {amount} into the account. New balance is {self.__account_balance}."
    else:
      return "Invalid deposit amount. Please deposit a positive amount."

  def withdraw(self, amount):
    if 0 < amount <= self.__account_balance:
      self.__account_balance -= amount
      return f"Withdrew {amount} from the account. New balance is {self.__account_balance}."
    elif amount > self.__account_balance:
      return "Insufficient funds for withdrawal."
    else:
      return "Invalid withdrawal amount. Please withdraw a positive amount."

  def display_balance(self):
    return f"Account balance for {self.__account_holder_name}: {self.__account_balance}"


# Testing the BankAccount class
if __name__ == "__main__":
  account = BankAccount("12345", "John Doe", 1000.0)

  print(account.display_balance())  # Display initial balance
  print(account.deposit(500))  # Deposit 500
  print(account.withdraw(200))  # Withdraw 200
  print(account.display_balance())  # Display updated balance
  print(account.withdraw(2000))  # Attempt to withdraw more than balance
  print(account.deposit(-100))  # Attempt to deposit a negative amount
