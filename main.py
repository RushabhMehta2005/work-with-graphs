from graph import Node, Graph, Edge
from traversals import *
from MST import *
from shortest_paths import *

V = [Node(val) for val in [0, 1, 2, 3, 4, 5, 6, 7, 8]]

directed_graph_data = [
    (0, 1, 4),
    (1, 2, 8),
    (2, 3, 7),
    (3, 4, 9),
    (4, 5, 10),
    (5, 6, 2),
    (6, 7, 1),
    (7, 0, 8),
    (1, 7, 11),
    (7, 8, 7),
    (8, 2, 2),
    (6, 8, 6),
    (2, 5, 4),
    (5, 3, 14),
]

E = []
for start, end, weight in directed_graph_data:
    E.append(Edge(V[start], V[end], weight))
    E.append(Edge(V[end], V[start], weight))

G = Graph(V, E)

print(kruskal(G))
