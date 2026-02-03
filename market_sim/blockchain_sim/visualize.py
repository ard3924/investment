import matplotlib.pyplot as plt
from .node import Node



def simulate():
    a = Node("A")
    b = Node("B")
    c = Node("C")

    a.connect_peer(b)
    b.connect_peer(a)

    b.connect_peer(c)
    c.connect_peer(b)

    chain_lengths = []

    a.create_block(["PRICE_UP"])
    chain_lengths.append((len(a.blockchain.chain),
                          len(b.blockchain.chain),
                          len(c.blockchain.chain)))

    c.create_block(["PRICE_DOWN"])
    chain_lengths.append((len(a.blockchain.chain),
                          len(b.blockchain.chain),
                          len(c.blockchain.chain)))

    a.connect_peer(c)
    c.connect_peer(a)

    a.create_block(["VOLUME_SPIKE"])
    chain_lengths.append((len(a.blockchain.chain),
                          len(b.blockchain.chain),
                          len(c.blockchain.chain)))

    return chain_lengths


if __name__ == "__main__":
    data = simulate()
    steps = range(len(data))

    a_len = [d[0] for d in data]
    b_len = [d[1] for d in data]
    c_len = [d[2] for d in data]

    plt.plot(steps, a_len)
    plt.plot(steps, b_len)
    plt.plot(steps, c_len)

    plt.xlabel("Simulation step")
    plt.ylabel("Chain length")
    plt.title("Fork creation and resolution via longest-chain rule")
    plt.show()
