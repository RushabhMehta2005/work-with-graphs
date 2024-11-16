def print_path(G, s, v):
    if v == s:
        print(s)
    elif v.pred == None:
        print(f"No path from {s} to {v} exists.")
    else:
        print_path(G, s, v.pred)
        print(v)
