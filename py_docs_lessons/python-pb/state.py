#Suppose we want to model a bank account with support for deposit
#and withdraw operations. One way to do that is by using global st
#ate as shown in the following 

balance = 0

def deposit(amount):
	global balance
	balance += amount
	return balance

def withdraw(amount):
	global balance
	balance-= amount
	return balance

class BankAccount:
	def __init__(self):
		self.balance -= amount
		return self.balance

	def withdraw(self, amount):
		self.balance -= amount
		return self.balance

	def deposit(self, amount):
		self.balance += amount
		return self.balance

robert = BankAccount()
vincent = BankAccount()

robert.deposit(100)
robert.withdraw(50)

