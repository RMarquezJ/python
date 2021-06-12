class User:
  
  def __init__(self,name,email):
    self.name = name
    self.email= email
    self.account_balance=0

  def make_deposit(self,amount):
    self.account_balance += amount

  def make_withdraw(self,amount):
    self.account_balance -= amount

  def display_user_balance(self):
    print('User: ' + self.name + ', Balance :' + str(self.account_balance))

  def transfer_money(self, receiver, amount):
    if self.account_balance>=amount:
      self.account_balance -= amount
      receiver.account_balance += amount
    else:
      print('Insuficcient balance')

guido = User('Guido van Rossum', 'guido@python.com')
monty = User('Monty Python', 'monty@python.com')
pedro = User('Pedro Picapiedra', 'pedro@python.com')

guido.make_deposit(100)
guido.make_deposit(500)
guido.make_deposit(300)

guido.make_withdraw(200)

guido.display_user_balance()

monty.make_deposit(200)
monty.make_deposit(300)

monty.make_withdraw(100)
monty.make_withdraw(500)

monty.display_user_balance()

pedro.make_deposit(1000)

pedro.make_withdraw(500)
pedro.make_withdraw(400)
pedro.make_withdraw(100)

pedro.display_user_balance()

guido.transfer_money(pedro, 500)

guido.display_user_balance()
pedro.display_user_balance()

guido.transfer_money(pedro,500)


