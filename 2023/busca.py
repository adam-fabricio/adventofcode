import heapq

LEFT = [1, 3, 2, 0]
XDIR = [-1, 0, 1, 0]
YDIR = [0, -1, 0, 1]

def close(n, visited):
    idx = n['x'] + n['y'] * S + n['dir'] * S * S + n['len'] * S * S * 4
    bitmask = 1 << (n['y'] & 7)
    if visited[n['y'] >> 3] & bitmask:
        return True
    visited[n['y'] >> 3] |= bitmask
    return False

def close_worse(n, visited):
    if close(n, visited):
        return True
    if n['len'] < 4:
        return False
    for i in range(n['len'] + 1, 11):
        if not close({'x': n['x'], 'y': n['y'], 'dir': n['dir'], 'len': i}, visited):
            return False
    return False

def insert(n, pq, node_alloc):
    i = (n['dist'] - n['x'] - n['y']) & 15
    pq[i].append(node_alloc)
    node_alloc += 1
    return node_alloc

def extract(pq, node_list):
    while not pq[P]:
        P = (P + 1) & 15
    return node_list[pq[P].pop(0)]

def walk(n, d, l, x, y, map, pq, node_alloc):
    if map[y * S + x]:
        insert({'x': x, 'y': y, 'dir': d, 'len': l, 'dist': n['dist'] + map[y * S + x]}, pq, node_alloc)

S = 144
map = [0] * (S * 144)
w, h, P, visited = 0, 0, 0, bytearray(18)
pq = [[] for _ in range(16)]
node_list = [{'x': 1, 'y': 1, 'dir': 0, 'len': 0, 'dist': 0}]
node_alloc = 1

with open('in17.txt', 'r') as f:
    for line in f:
        for c in line.strip():
            map[h * S + w] = int(c)
            w += 1
        h += 1
        w = 0

while True:
    n = extract(pq, node_list)
    if not close_worse(n, visited):
        if n['x'] == w and n['y'] == h:
            break
        X, Y = XDIR[n['dir']], YDIR[n['dir']]
        if n['len'] < 10:
            walk(n, n['dir'], n['len'] + 1, n['x'] + X, n['y'] + Y, map, pq, node_alloc)
        if n['len'] >= 4:
            X, Y = Y, -X
            d = LEFT[n['dir']]
            walk(n, d, 1, n['x'] + X, n['y'] + Y, map, pq, node_alloc)

print(f"A distância do caminho mais curto é {node_list[-1]['dist']}.")

