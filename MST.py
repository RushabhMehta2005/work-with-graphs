def kruskal(G):
    """
    Implementation of kruskal's algorithm for finding Minimum Spanning Tree.

    Args:
        G: Graph with undirected edges
    Returns:
        Tuple: mst: List[Edge], total_mst_cost: int
    """

    edges = sorted(G.E, key=lambda edge: edge.weight)
    parent = {u: u for u in G.V}

    def find_parent(u):
        if u != parent[u]:
            parent[u] = find_parent(parent[u])
        return parent[u]

    total_mst_cost = 0
    mst = []

    for edge in edges:
        u, v, w = edge.start, edge.end, edge.weight
        parent_u = find_parent(u)
        parent_v = find_parent(v)
        if parent_u != parent_v:
            total_mst_cost += w
            mst.append(edge)
            parent[parent_u] = parent_v

    return mst, total_mst_cost


def prim(G, s=None):
    """
    Implementation of prim's algorithm for finding Minimum Spanning Tree.

    Args:
        G: Undirected, Connected non-negative weight graph G
        s: starting node (if not provided, will be set as G.V[0]) 

    Returns:
        Tuple: mst: List[Edge], total_mst_cost: int
    """
    
    key = {}
    for v in G.V:
        key[v] = float("inf")
        v.pred = None
    
    if s is None:
        s = G.V[0]
    key[s] = 0

    # TODO












