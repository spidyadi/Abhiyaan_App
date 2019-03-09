import sys
import copy

class Transaction:
	reciever = {}
	sender = {}
	amount = 0

	def __init__(self, sender, reciever, amount):
		self.reciever = reciever
		self.sender = sender
		self.amount = amount
	def __str__(self):
		return str(self.sender) + " pays " + str(self.reciever) + " " + str(self.amount)
	def __repr__(self):
		return str(self.sender) + " pays " + str(self.reciever) + " " + str(self.amount)


class Person:
	balance = 0
	owes = {}
	name = ""
	def __init__(self, name):
		self.name = str(name)

	def transact(self, friend, money):
		if friend not in self.owes.keys():
			self.owes[friend] = 0
		self.balance += money
		self.owes[friend] += money

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.name

class Splitwise:
	transactions = []
	people = []

	def __init__(self):
		self.transactions = []
		self.people = []

	# adds a transaction between sender and reciever
	# if they don't exist, it creates an account for the sender and reciever
	def add_transaction(self, sender, reciever, money):
		if not isinstance(sender, Person):
			found_sender = False
			for person in self.people:
				if person.name == sender:
					sender = person
					found_sender = True
			if not found_sender:
				sender = Person(sender)
				self.people.append(sender)
		if not isinstance(reciever, Person):
			found_reciever = False
			for person in self.people:
				if person.name == reciever:
					reciever = person
					found_reciever = True
			if not found_reciever:
				reciever = Person(reciever)
				self.people.append(reciever)
		t = Transaction(sender, reciever, money)
		self.transactions.append(t)
		sender.transact(reciever, money)
		reciever.transact(sender, ((-1)*money))

	# accepts a list of people
	# checks if everything is settled between everyone
	@staticmethod
	def is_balanced(people):
		for person in people:
			if person.balance != 0:
				return False
		return True

	# gets the minimal nunumber of transactions to settle debts
	# calls minimize_transactions and implements it
	def settle_things(self):
		transactions = self.minimize_transactions()
		sender = None
		reciever = None
		for transaction in transactions:
			for person in self.people:
				if person.name == transaction.reciever.name:
					reciever = person
				if person.name == transaction.sender.name:
					sender = person
			sender.transact(reciever, transaction.amount)
			reciever.transact(sender, (-1)*transaction.amount)
			self.transactions.append(Transaction(sender, reciever, transaction.amount))

	# this function is supposed to return minimal number of transactions to settle debts
	# Creates a deep copy of the list of people involved.
	# and then recursively calls settle_max_min (Greedy approach),
	# reducing number of people owing one (or more) person at a time.
	def minimize_transactions(self):
		copy_people = []
		for person in self.people:
			copy_people.append(copy.deepcopy(person))
		settle_transactions = []

		while not self.is_balanced(copy_people):
			settle_transactions.append(self.settle_max_min(copy_people))

		return settle_transactions

	# Takes a list of people and finds:
	# 	1. the person who owes the most (min_per)
	# 	2. the person who owes the least (max_per)
	# and then creates a transaction between them and then returns that transaction.
	@staticmethod
	def settle_max_min(people):
		min_bal = sys.maxsize
		min_per = None
		max_bal = -sys.maxsize -1
		max_per = None

		for person in people:
			if person.balance > max_bal:
				max_per = person
				max_bal = person.balance
			if person.balance < min_bal:
				min_per = person
				min_bal = person.balance

		trans_amount = min(abs(min_bal), max_bal)
		t = Transaction(min_per, max_per, trans_amount)
		min_per.transact(max_per, trans_amount)
		max_per.transact(min_per, ((-1)*trans_amount))

		return t

print("Hello! Welcome to Mini-Splitwise.. Here you can add transactions between people. \n")
s = Splitwise()
option = 0
while not option == 6:
	
	# type checks if input is valid
	try:
		option = int(input("Choose an option: (1) to add transaction (2) view existing transactions (3) See What people owe (4) See quickest way to settle debts (5) Settle things now. (6) Exit \n"))
		if (option > 6) or (option < 1):
			print("Enter an integer between 1 and 6\n")
			continue
	except ValueError:
		print("You didn't even enter an integer!!\n")
		continue

	# Exits program
	if option == 6:
		print("Thank you for using Mini-Splitwise! Bye! \n")
		break

	# Settles things between people
	if option == 5:
		s.settle_things()
		print("All settled!")

	# Shows minimum number of transactions required to settle things
	if option == 4:
		transactions = s.minimize_transactions()
		if len(transactions) == 0:
			print("No settlement needed! \n")
		for transaction in transactions:
			print(transaction)

	# Show what people owe or what they are owed
	if option == 3:
		if len(s.people) == 0:
			print("No people yet! \n")
		for person in s.people:
			if person.balance > 0:
				print(person.name + " is owed "+ str(person.balance))
			else:
				print(person.name + " owes "+ str(abs(person.balance)))

	# Show history of transactions
	if option == 2:
		if len(s.transactions) == 0:
			print("No transactions yet! \n")
		for transaction in s.transactions:
			print(transaction)

	# Add a transaction
	if option == 1:
		sender = input("Who paid? \n")
		reciever = input("Who recieved? \n")
		try:
			amount = int(input("How much? \n"))
			if (amount < 0):
				print("Enter an integer greater than 0!\n")
				continue
			s.add_transaction(sender, reciever, amount)
		except ValueError:
			print("You didn't even enter an integer!!\n")
			continue


