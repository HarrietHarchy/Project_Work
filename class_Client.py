class Customer(object):

	def __init__(self,name,balance=0.0):

		self.name=name
		self.balance=balance

	def withdraw(self,amount):

			if amount>self.balance:
				self.balance -=amount

				return "insufficient balance"

			elif amount<self.balance:
				self.balance -=amount
				return self.balance
					
	def deposit(self,amount):
		self.balance +=amount

		return self.balance

	def checkbalance(self):
		return self.balance


Harriet=Customer('Harriet',400)
print(Harriet.checkbalance())

print(Harriet.withdraw(500))
print(Harriet.checkbalance())

print(Harriet.deposit(1000))
print(Harriet.checkbalance())

print(Harriet.withdraw(800))
print(Harriet.checkbalance())

	




	



