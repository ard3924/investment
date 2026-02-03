from blockchain import Blockchain


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.blockchain = Blockchain()
        self.peers = []

    def connect_peer(self, peer):
        self.peers.append(peer)

    def create_block(self, events):
        self.blockchain.add_block(events)
        self.broadcast_chain()

    def broadcast_chain(self):
        for peer in self.peers:
            peer.receive_chain(self.blockchain.chain)

    def receive_chain(self, incoming_chain):
        if len(incoming_chain) > len(self.blockchain.chain):
            self.blockchain.chain = incoming_chain

# Example usage
if __name__ == "__main__":
    a = Node("A")
    b = Node("B")
    c = Node("C")

    # Connect peers
    a.connect_peer(b)
    b.connect_peer(a)

    b.connect_peer(c)
    c.connect_peer(b)

    # A and C mine independently (fork)
    a.create_block(["PRICE_UP"])
    c.create_block(["PRICE_DOWN"])

    # Now connect A and C to resolve fork
    a.connect_peer(c)
    c.connect_peer(a)

    # One more block from A to win longest chain
    a.create_block(["VOLUME_SPIKE"])

    print("A chain length:", len(a.blockchain.chain))
    print("B chain length:", len(b.blockchain.chain))
    print("C chain length:", len(c.blockchain.chain))

