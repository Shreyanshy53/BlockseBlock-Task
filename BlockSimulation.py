import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

def create_genesis_block():
    return Block(0, time.time(), "Genesis Block", "0")

def create_next_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = time.time()
    previous_hash = previous_block.hash
    return Block(index, timestamp, data, previous_hash)

# Create the blockchain with 3 blocks
blockchain = [create_genesis_block()]
blockchain.append(create_next_block(blockchain[-1], "Block 1 Data"))
blockchain.append(create_next_block(blockchain[-1], "Block 2 Data"))

# Display all blocks with their hashes
for block in blockchain:
    print(f"Block #{block.index}")
    print(f"Timestamp     : {block.timestamp}")
    print(f"Data          : {block.data}")
    print(f"Previous Hash : {block.previous_hash}")
    print(f"Nonce         : {block.nonce}")
    print(f"Hash          : {block.hash}")
    print("-" * 50)

