
import hashlob
import json
from time import time


class Blockchain(object):
	def __init__(self):
		self.chain = []
		self.current_transactions = []

	def new_block(self, proof, previous_hash=None):
		#Creates a new block in the blockchain
		pass

	def new_transaction(self, sender, recipient, amount):
		#sender - address of the sender(string)
		#recipient - address of the recipient(string)
		#amount - amount (int)
		#return : Index of the block that holds this transaction(int)
		self.current_transactions.append({
			'sender':sender,
			'recipient':recipient,
			'amount':amount,
			})

		return self.last_block['index'] + 1

	@staticmethod
	def hash(block):
		pass

	def last_block(self):
		pass
