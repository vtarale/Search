# Search
plotting of graphs, a star search, greedy best search and bfs and dfs lib

## importing the libs
```python
import search.breath_first_search as bfs
import search.depth_first_search as dfs
import search.a_star_search as a_star
import search.greedy_best_first_search as gbfs
```

## creating nodes
```python
# a star search
a = a_star.Node(parameters)
# same applys for others
```

## joining nodes
```python
# a is a node
a.n = [other nodes]
```

## searching
```python
# Ex
bfs.bfs(a, h)
```
## Running
 ```bash
 python <name>.py
 ```
## License    
[apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)
