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

    def mine_block(self, difficulty):
        print(f"⛏️ Mining Block {self.index}...")

        start_time = time.time()
        prefix_str = '0' * difficulty

        while not self.hash.startswith(prefix_str):
            self.nonce += 1
            self.hash = self.compute_hash()

        end_time = time.time()
        print(f" Block {self.index} mined!")
        print(f"Hash         : {self.hash}")
        print(f"Nonce        : {self.nonce}")
        print(f"Time taken   : {end_time - start_time:.4f} seconds")
        print("-" * 50)

# Blockchain setup with mining
difficulty = 4  # Adjust this for more/less difficulty

def create_genesis_block():
    block = Block(0, time.time(), "Genesis Block", "0")
    block.mine_block(difficulty)
    return block

def create_next_block(prev_block, data):
    block = Block(prev_block.index + 1, time.time(), data, prev_block.hash)
    block.mine_block(difficulty)
    return block

# Build blockchain with mining
blockchain = [create_genesis_block()]
blockchain.append(create_next_block(blockchain[-1], "Block 1 Data"))
blockchain.append(create_next_block(blockchain[-1], "Block 2 Data"))
