# Blockchain
Creating a Basic Local Blockchain on Python

This was a personal project to grasp the concepts of Blockchain and creating a basic blockchain.

The Blockchain is represented as an object for the implementation in order to create specific attributes, methods and instances.
A Block contains Timestamp, Transaction, Hash, Previous Hash and Nonce.
Hashing is done with the SHA-256 algorithm from the hashlib library. The output is random but deterministic.
A Blockchain contains a Chain, Unverified Transacation and a Genesis Block.
The Genesis Block is the first block in a Blockchain and is hard-coded.
We can check for a broken chain through the validation of the hashing.
A Proof-of-Work is a security feature going through each block to prevent attackers from taking over the blockchain.
A nonce is a number combined with the block and hashed to be guessed by the miners.
Actual blockchains operate on multiple computers in a decentralized manner.
