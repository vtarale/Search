from math import sqrt
from sys import exit

def py_therom(x1, y1, x2, y2):
    d1 = abs(x1-x2)
    d2 = abs(y1-y2)
    return sqrt((d1 ** 2) + (d2 ** 2))

class Node:
    def __init__(self, x, y, n, data):
        self.x = x
        self.y = y
        self.n = n
        self.data = data
        self.parent = None

    def add(self, node):
        self.n.append(node)

    def set_parent(self, parent):
        self.parent = parent

    def distance(self, node):
        return py_therom(self.x, self.y, node.x, node.y)

def find_path(found):
    path = []
    node_path = []
    temp = found
    while temp != None:
        path.append(temp.data)
        node_path.append(temp)
        temp = temp.parent
    path.reverse()
    node_path.reverse()
    print(path)
    return node_path

def a_star_search(root, find):
    temp = root

    explored = []
    to_explore = []
    steps = 0

    while True:
        total = []
        if temp == find:
            find_path(temp)
            print(f"Steps: {steps}")
            exit(1)

        for node in temp.n:
            if node not in explored:
                if node != root:
                    node.set_parent(temp)
                    to_explore.append(node)

        for node in to_explore:
            total.append(temp.distance(node) + temp.distance(find))

        min = total[0]
        for index in range(len(total)):
            if min > total[index]:
                min = total[index]

        index = total.index(min)
        explored.append(to_explore[index])
        temp = to_explore[index]
        steps += 1

        for node in to_explore:
            if node in explored:
                del to_explore[to_explore.index(node)]