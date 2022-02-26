import matplotlib.pyplot as plt

def plot(root, find, nodes, cord=True):
    explored = []
    if cord:
        x = []
        y = []
        for node in nodes:
            x.append(node.x)
            y.append(node.y)
        plt.scatter(x, y)

        for node in nodes:
            for n in node.n:
                if node in explored:
                    continue
                plt.plot([node.x, n.x], [node.y, n.y])
            explored.append(node)

        plt.show()