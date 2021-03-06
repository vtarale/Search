import sys


class Node:
    def __init__(self, val):
        self.val = val
        self.n = []
        self.parent = None
    def set_parent(self, parent):
        self.parent = parent
    def add(self, node):
        self.n.append(node)

class Queue:
    def __init__(self):
        self.q = []
    def add(self, node):
        self.q.append(node)
    def get(self):
        node = self.q[0]
        self.q = self.q[1:]
        return node
    def isempty(self):
        if len(self.q) == 0:
            return True
        return False

class Explore(Queue):
    def get(self):
        pass
    def check(self, node):
        if node in self.q:
            return True
        return False

def bfs(root, find):
    temp = root
    q = Queue()
    e = Explore()
    q.add(temp)
    temp.set_parent(None)

    while True:
        if q.isempty():
            print("No solution!!")
            sys.exit(0)
        
        temp = q.get()
        if e.check(temp):
            continue

        e.add(temp)

        for i in temp.n:
            if e.check(i):
                continue
            i.set_parent(temp)
            if i == find:
                temp = i
                print("Soluiton Found:")
                find_path(temp)
                return
            q.add(i)

def find_path(node):
    temp = node
    path = []

    while temp != None:
        path.append(temp.val)
        temp = temp.parent
    path.reverse()
    print(path)