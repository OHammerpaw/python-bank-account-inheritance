class BankAccount:
  def __init__(self, balance=0 self.interest_rate= .02):
    self.balance = balance

  def __str__(self):
    status = f"balance: {self.balance}"
    return status

  def deposit(self, amount):
    if amount < 0: return False
    self.balance += amount
    return self.balance

  def withdraw(self, amount):
    if amount < 0: return False
    self.balance -= amount
    return self.balance

  def accumulate_interest(self):
    self.balance += self.balance * self.interest_rate
    return self.balance

class ChildrensAccount:
  def __init__(self):
    super().__init__()
    self.interst_rate = 0

  def accumulate_interest(self):
    self.balance += 10
    return self.balance

class OverdraftAccount(BankAccount):
  def __init__(self):
    self.overdraft_penalty = 40
    return super().__init__()

  def withdraw(self, amount):
    result = self.balance - amount
    if result < 0:
      self.balance -= 40
      return False

    super().withdraw(amount)

  def accumulate_interest(self):
    if self.balance < 0: return False
    return super().accumulate_interest()

basic_account = BankAccount()
basic_account.deposit(600)
print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(17)
print("Basic account has ${}".format(basic_account.balance))
basic_account.accumulate_interest()
print("Basic account has ${}".format(basic_account.balance))
print()

childs_account = ChildrensAccount()
childs_account.deposit(34)
print("Child's account has ${}".format(childs_account.balance))
childs_account.withdraw(17)
print("Child's account has ${}".format(childs_account.balance))
childs_account.accumulate_interest()
print("Child's account has ${}".format(childs_account.balance))
print()

overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print("Overdraft account has ${}".format(overdraft_account.balance))
