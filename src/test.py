import search.breath_first_search as bfs
import search.depth_first_search as dfs
import search.a_star_search as a_star
import search.greedy_best_first_search as gbfs
import matplotlib.pyplot as pyt # type: ignore

a_list = [10, 50]
b_list = [30, 90]
c_list = [50, 70]
d_list = [60, 10]
e_list = [80, 50]

xcor = [a_list[0], b_list[0], c_list[0], d_list[0], e_list[0]]
ycor = [a_list[1], b_list[1], c_list[1], d_list[1], e_list[1]]

pyt.scatter(xcor, ycor, color="cyan")   
pyt.plot([a_list[0], b_list[0]], [a_list[1],b_list[1]], color="cyan")
pyt.plot([a_list[0], d_list[0]], [a_list[1],d_list[1]], color="cyan")
pyt.plot([c_list[0], b_list[0]], [c_list[1],b_list[1]], color="cyan")
pyt.plot([d_list[0], b_list[0]], [d_list[1],b_list[1]], color="cyan")
pyt.plot([c_list[0], e_list[0]], [c_list[1],e_list[1]], color="cyan")
pyt.plot([d_list[0], e_list[0]], [d_list[1],e_list[1]], color="cyan")

def check(x):
    if x == 'a':
        return a_list
    elif x == 'b':
        return b_list
    elif x == 'c':
        return c_list
    elif x == 'd':
        return d_list
    else:
        return e_list

a = a_star.Node(a_list[0], a_list[1], None, 'a')
b = a_star.Node(b_list[0], b_list[1], None, 'b')
c = a_star.Node(c_list[0], c_list[1], None, 'c')
d = a_star.Node(d_list[0], d_list[1],None, 'd')
e = a_star.Node(e_list[0], e_list[1],None, 'e')
a.n = [b, d]
b.n = [a, c, d]
c.n = [b, e]
d.n = [a, e, b]
e.n = [c, d]
print("A star search")
ans = a_star.a_star_search(a, e)
temp = ans[0]
for i in range(1, len(ans)):
    x_list = check(temp)
    y_list = check(ans[i])
    temp = ans[i]
    pyt.plot([x_list[0], y_list[0]], [x_list[1],y_list[1]], color="green")
#print(ans)

a = gbfs.Node(a_list[0], a_list[1], None, 'a')
b = gbfs.Node(b_list[0], b_list[1], None, 'b')
c = gbfs.Node(c_list[0], c_list[1], None, 'c')
d = gbfs.Node(d_list[0], d_list[1],None, 'd')
e = gbfs.Node(e_list[0], e_list[1],None, 'e')
a.n = [b, d]
b.n = [a, c, d]
c.n = [b, e]
d.n = [a, e, b]
e.n = [c, d]
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
pyt.show()