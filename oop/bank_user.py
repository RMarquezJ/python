class BankAccount:
  def __init__(self, int_rate=0.01, balance=0):
    self.int_rate = int_rate
    self.balance = balance
  
  def deposit(self,amount):
    self.balance += amount
    return self
  
  def withdraw(self, amount):
    if self.balance >= amount:
      self.balance -= amount
      return self
    else:
      print('Insufficient balance')
  
  def display_account_info(self):
    print('Balance :' + str(round(self.balance)))
  
  def yield_balance(self):
    if self.balance > 0:
      self.balance *= (1 + self.int_rate)
      return self
    else:
      pass

class User:
  
  def __init__(self,name,email):
    self.name = name
    self.email = email
    self.accounts = [BankAccount(0.05)]

  def make_deposit(self,amount,num):
    self.accounts[num].deposit(amount)
    return self

  def make_withdraw(self,amount,num):
    self.accounts[num].withdraw(amount)
    return self

  def display_user_balance(self,num):
    print('User: ' + self.name + ', Balance :' + str(self.accounts[num].balance))

  def transfer_money(self, receiver, amount, num):
    if self.accounts[num].balance >= amount:
      self.accounts[num].withdraw(amount)
      receiver.accounts[0].deposit(amount)
    else:
      print('Insuficcient balance')
  
  def create_account(self):
    self.accounts.append(BankAccount(0.05))

guido = User('Guido van Rossum', 'guido@python.com')
monty = User('Monty Python', 'monty@python.com')
pedro = User('Pedro Picapiedra', 'pedro@python.com')

guido.create_account()
guido.make_deposit(100,0)
guido.make_deposit(500,0)
guido.make_deposit(300,1)

guido.make_withdraw(200,1)

guido.display_user_balance(1)

monty.make_deposit(200,0)
monty.make_deposit(300,0)

monty.make_withdraw(100,0)
monty.make_withdraw(500,0)

monty.display_user_balance(0)

pedro.make_deposit(1000,0)

pedro.make_withdraw(500,0)
pedro.make_withdraw(400,0)
pedro.make_withdraw(100,0)

pedro.display_user_balance(0)

guido.transfer_money(pedro, 500,0)

guido.display_user_balance(0)
pedro.display_user_balance(0)

guido.transfer_money(pedro,500,0)

guido.make_deposit(100,0).make_deposit(500,0).make_withdraw(300,0).display_user_balance(0)