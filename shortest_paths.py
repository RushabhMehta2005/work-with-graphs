import heapq


def djikstra(G, s):
    """
    Single source shortest paths algorithm. Finds minimum distance of all nodes from source node.
    Assumes all weights are non-negative.
    Args:
        G: graph (type: Graph)
        s: source vertex (type: Node)

    Returns: None
    """
    s.dist = 0
    s.color = "GRAY"

    # the elements of the heap are of the form (u.dist, u) as
    # the heapq module does not allow for a dynamic priority change
    heap = [(0, s)]
    heapq.heapify(heap)

    while heap:
        # dist_u is just u.dist and its best to leave it unused
        dist_u, u = heapq.heappop(heap)

        for v in G.Adj[u]:
            if v.dist > u.dist + G.w[(u, v)]:
                v.dist = u.dist + G.w[(u, v)]
                v.pred = u
                v.color = "GRAY"
                heapq.heappush(heap, (v.dist, v))

        u.color = "BLACK"
