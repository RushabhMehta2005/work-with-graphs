from collections import defaultdict
from tabulate import tabulate


class Node:
    def __init__(self, val):
        self.val = val
        self.pred = None
        self.color = "WHITE"

        # for BFS
        self.dist = float("inf")

        # for DFS
        self.discovery = None
        self.finish = None

    def __repr__(self):
        return f"Node {self.val}"

    def _clear_node_data(self):
        self.pred = None
        self.color = "WHITE"
        self.dist = None
        self.discovery = None
        self.finish = None


class Graph:
    def __init__(self, V, E):
        self.V = V
        self.E = E
        self.w = {}
        self.Adj = self.build_adj()

    def build_adj(self):
        adj = defaultdict(list)
        for edge in self.E:
            start, end, weight = edge.start, edge.end, edge.weight
            adj[start].append(end)
            self.w[(start, end)] = weight
        return adj

    def weight(self, start, end):
        """Returns the weight between start and end vertices if there exists a direct edge, else infinity."""
        return self.w.get((start, end), float("inf"))

    def _clear_graph(self):
        for node in self.V:
            node._clear_node_data()

    def __str__(self):
        headers = ["Node", "Predecessor", "Distance", "Color"]
        table = [
            [
                node.val,
                node.pred.val if node.pred else "NIL",
                node.dist if node.dist is not None else "inf",
                node.color,
            ]
            for node in self.V
        ]

        return tabulate(table, headers=headers, tablefmt="fancy_grid")


class Edge:
    """
    Represents a directed weighted edge.
    If weight is not supplied, it is set as 1.
    """

    def __init__(self, start: Node, end: Node, weight=1):
        self.start = start
        self.end = end
        self.weight = weight

    def __repr__(self):
        return f"({self.start} → {self.end}) [Weight: {self.weight}]"
