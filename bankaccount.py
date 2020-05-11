class Account():
	Balance=100
	def __init__(self,Owner,Balance):
		self.Owner=Owner
		self.Balance=Balance
	def deposite(self,deposite_ammount):
		
		self.Balance+=deposite_ammount
		print(f'You have successfully deposited ${deposite_ammount} and your total Balance is {self.Balance}')
	def withdrawl(self,withdrawl_ammount):
		
		if self.Balance>=withdrawl_ammount:
			self.Balance-=withdrawl_ammount
		else:
			print('Insufficient Balance')
		print(f'${withdrawl_ammount} has been debited and your remeaining Balance is {self.Balance}')
	def __str__(self):
		return f'Account Owner: {self.Owner} \nBalance: {self.Balance}'

a=Account('Rushi',500)
print(a)
print(a.Owner)
print(a.Balance)
a.deposite(200)
a.withdrawl(100)
print(a)

		

