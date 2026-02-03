import hashlib
import time


class Block:
    def __init__(self, index, prev_hash, events, timestamp=None):
        self.index = index
        self.prev_hash = prev_hash
        self.events = events  # list of market events (strings for now)
        self.timestamp = timestamp or time.time()
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.index}{self.prev_hash}{self.events}{self.timestamp}"
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", ["GENESIS"])

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, events):
        latest = self.get_latest_block()
        new_block = Block(
            index=latest.index + 1,
            prev_hash=latest.hash,
            events=events
        )
        self.chain.append(new_block)

    def is_longest_chain(self, other_chain):
        return len(other_chain) > len(self.chain)
