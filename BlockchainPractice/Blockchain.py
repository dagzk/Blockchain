# import datetime library
from datetime import datetime
# import sha256
from hashlib import sha256
from Block import Block
# print current date and time
print(datetime.now())

# transaction1 = {
#   'amount': '30',
#   'sender': 'Alice',
#   'receiver': 'Bob'}
# transaction2 = {
#   'amount': '200',
#   'sender': 'Bob',
#   'receiver': 'Alice'}
# transaction3 = {
#   'amount': '300',
#   'sender': 'Alice',
#   'receiver': 'Timothy' }
# transaction4 = {
#   'amount': '300',
#   'sender': 'Rodrigo',
#   'receiver': 'Thomas' }
# transaction5 = {
#   'amount': '200',
#   'sender': 'Timothy',
#   'receiver': 'Thomas' }
# transaction6 = {
#   'amount': '400',
#   'sender': 'Tiffany',
#   'receiver': 'Xavier' }
#
# mempool = [transaction1, transaction2, transaction3, transaction4, transaction5, transaction6]
#
# # Create own transaction
#
# my_transaction = {
#   'amount': '777',
#   'sender': 'Dan',
#   'receiver': 'Diana' }

# Add my transaction to mempool
# mempool = [transaction1, transaction2, transaction3, transaction4, transaction5, transaction6, my_transaction]

# Simpler Method
# mempool = mempool.append(my_transaction)

# Create a new list for future Block Structure
# block_transactions = [transaction1, transaction3, my_transaction]

# Example text to hash
# text = "I am making a blockchain"

# print result

# hash_result = sha256(text.encode())
# print(hash_result.hexdigest())

class Blockchain:
  def __init__(self):
    self.chain = []
    self.unconfirmed_transactions = []
    self.genesis_block()

  def genesis_block(self):
    transactions = []
    genesis_block = Block(transactions, "0")
    genesis_block.generate_hash()
    self.chain.append(genesis_block)

  def add_block(self, transactions):
    previous_hash = (self.chain[len(self.chain) - 1]).hash
    new_block = Block(transactions, previous_hash)
    new_block.generate_hash()
    proof = self.proof_of_work(new_block)
    self.chain.append(new_block)
    return proof, new_block

  def print_blocks(self):
    for i in range(len(self.chain)):
      current_block = self.chain[i]
      print("Block {} {}".format(i, current_block))
      current_block.print_contents()

  def validate_chain(self):
    for i in range(1, len(self.chain)):
      current = self.chain[i]
      previous = self.chain[i - 1]
      if (current.hash != current.generate_hash()):
        print("The current hash of the block does not equal the generated hash of the block.")
        return False
      if (current.previous_hash != previous.generate_hash()):
        print("The previous block's hash does not equal the previous hash value stored in the current block.")
        return False
    return True

  def proof_of_work(self, block, difficulty=2):
    proof = block.generate_hash()
    while proof[:difficulty] != '0' * difficulty:
      block.nonce += 1
      proof = block.generate_hash()
    block.nonce = 0
    return proof