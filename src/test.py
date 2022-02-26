import search.breath_first_search as bfs
import search.depth_first_search as dfs
import search.a_star_search as a_star
import search.greedy_best_first_search as gbfs

a = a_star.Node(20, 30, None, 'a')
b = a_star.Node(40, 50, None, 'b')
c = a_star.Node(1, 2, None, 'c')
d = a_star.Node(45, 56, None, 'd')
e = a_star.Node(67, 68, None, 'e')
a.n = [b, c]
b.n = [a, d, e]
c.n = [a, d]
d.n = [b, c]
e.n = [b]
print("A star search")
a_star.a_star_search(a, e)

a = gbfs.Node(20, 30, None, 'a')
b = gbfs.Node(40, 50, None, 'b')
c = gbfs.Node(1, 2, None, 'c')
d = gbfs.Node(45, 56, None, 'd')
e = gbfs.Node(67, 68, None, 'e')
a.n = [b, c]
b.n = [a, d, e]
c.n = [a, d]
d.n = [b, c]
e.n = [b]
print("Greedy Best Search: ")
gbfs.greedy_best_first_search(a, e)

a = bfs.Node('a')
b = bfs.Node('b')
c = bfs.Node('c')
d = bfs.Node('d')
e = bfs.Node('e')
f = bfs.Node('f')
g = bfs.Node('g')
h = bfs.Node('h')
a.n = [b, c, d, g]
b.n = [a, h]
c.n = [a, e]
d.n = [a, f]
e.n = [c, f]
f.n = [d, e, h]
g.n = [a]
h.n = [f, b]
print("Bfs:")
bfs.bfs(g, f) 

a = dfs.Node('a')
b = dfs.Node('b')
c = dfs.Node('c')
d = dfs.Node('d')
e = dfs.Node('e')
f = dfs.Node('f')
g = dfs.Node('g')
h = dfs.Node('h')
a.n = [b, c, d, g]
b.n = [a, h]
c.n = [a, e]
d.n = [a, f]
e.n = [c, f]
f.n = [d, e, h]
g.n = [a]
h.n = [f, b]
print("Dfs:")
dfs.dfs(g, f) 