from collections import deque as queue


def bfs(G, s):
    """
    Performs a simple breadth-first search of the given graph.
    Calculates distance from source vertex s and predecessor for each vertex.
    Args:
        G: Graph

    Returns:
        None
    """
    for u in G.V:
        if u != s:
            u.color = "WHITE"
            u.dist = float("inf")
            u.pred = None

    s.color = "GRAY"
    s.dist = 0
    s.pred = None

    Q = queue()
    Q.append(s)

    while Q:
        u = Q.popleft()

        for v in G.Adj[u]:
            if v.color == "WHITE":
                v.color = "GRAY"
                v.dist = u.dist + 1
                v.pred = u
                Q.append(v)
        u.color = "BLACK"


def dfs(G):
    """
    Performs a simple depth-first search of the given graph.
    Calculates discovery time, finish time and predecessor for each vertex.
    Args:
        G: Graph

    Returns:
        None
    """

    def dfs_visit(u):
        nonlocal time
        time += 1
        u.discovery = time
        u.color = "GRAY"
        for v in G.Adj[u]:
            if v.color == "WHITE":
                v.pred = u
                dfs_visit(v)
        u.color = "BLACK"
        time += 1
        u.finish = time

    for u in G.V:
        u.color = "WHITE"
        u.pred = None

    time = 0
    for u in G.V:
        if u.color == "WHITE":
            dfs_visit(u)


def topological_sort(G):
    """
    Gives a topologically sorted sequence of vertices.
    Assumes given graph is connected.

    Args:
        G: Graph

    Returns:
        seq: Sequence of vertices in topologically sorted order.
    """
    dfs(G)
    seq = [v for v in G.V if v.finish]
    seq.sort(key=lambda v: -v.finish)
    return seq


def multi_source_bfs(G, criteria):
    """
    Performs multi source breadth first search on a graph,
    starting from the vertices which satisfy the criteria given.

    Args:
        G: Graph
        criteria: function -> bool

    Returns:
        None
    """

    Q = queue()

    for u in G.V:
        if criteria(u):
            u.color = "GRAY"
            u.dist = 0
            u.pred = None
            Q.append(u)
        else:
            u.color = "WHITE"
            u.dist = float("inf")
            u.pred = None

    while Q:
        u = Q.popleft()

        for v in G.Adj[u]:
            if v.color == "WHITE":
                v.color = "GRAY"
                v.dist = u.dist + 1
                v.pred = u
                Q.append(v)

        u.color = "BLACK"


def detect_cycle(G, algorithm="BFS"):
    """
    Returns True if there is a cycle in given graph G.
    Assumes G is undirected.
    Args:
        G: Graph
        algorithm: str ("BFS" or "DFS")
    
    Raises:
        ValueError if algorithm is invalid
        
    Returns:
        bool
    """
    if algorithm not in ["DFS", "BFS"]:
        raise ValueError(f"expected algorithm BFS or DFS but {algorithm} was given")

    for u in G.V:
        u.color = "WHITE"
        u.dist = float("inf")
        u.pred = None

    if algorithm == "BFS":

        def bfs_detect(s):
            s.color = "GRAY"
            s.dist = 0
            s.pred = None

            Q = queue()
            Q.append(s)

            while Q:
                u = Q.popleft()

                for v in G.Adj[u]:
                    if v.color == "GRAY" and v != u.pred:
                        return True
                    if v.color == "WHITE":
                        v.color = "GRAY"
                        v.dist = u.dist + 1
                        v.pred = u
                        Q.append(v)
                u.color = "BLACK"

            return False

        for u in G.V:
            if u.color == "WHITE" and bfs_detect(u):
                return True

        return False

    else:
        visited = set()

        def dfs_detect(u):
            visited.add(u)

            for v in G.Adj[u]:
                if v in visited and v != u.pred:
                    return True
                if v not in visited and dfs_detect(v):
                    return True

            return False

        for u in G.V:
            if u not in visited and dfs_detect(u):
                return True
        return False
