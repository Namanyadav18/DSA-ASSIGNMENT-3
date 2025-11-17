#!/usr/bin/env python3
from src.building import Building
from src.bst import BST
from src.avl import AVL
from src.graph import CampusGraph
from src.expression_tree import ExpressionTree

def demo():
    print("\n--- DEMO: Campus Navigation & Utility Planner (Python) ---\n")

    # sample buildings
    sample_buildings: List[Building] = [
        Building(3, 'Library', 'Block A'),
        Building(1, 'Admin', 'Block B'),
        Building(4, 'Cafeteria', 'Block C'),
        Building(2, 'CS Dept', 'Block D'),
        Building(5, 'Gym', 'Block E'),
    ]

    # BST
    bst = BST()
    for b in sample_buildings:
        bst.insert(b)
    print('BST inorder:', bst.inorder())
    print('BST preorder:', bst.preorder())
    print('BST postorder:', bst.postorder())
    print('BST height:', bst.height())

    # AVL
    avl = AVL()
    for b in sample_buildings:
        avl.insert(b)
    print('\nAVL inorder:', avl.inorder())
    print('AVL height:', avl.height())

    print('\nHeight comparison: BST vs AVL ->', bst.height(), 'vs', avl.height())

    # Graph
    # Map building IDs to compact indices for graph nodes (0..n-1)
    sorted_buildings = sorted(sample_buildings, key=lambda x: x.id)
    id_to_index = {b.id: i for i, b in enumerate(sorted_buildings)}
    index_to_id = {v: k for k, v in id_to_index.items()}
    n = len(sample_buildings)
    g = CampusGraph(n)

    # sample edges (u_id, v_id, weight)
    edges = [
        (1,2,1.5),
        (1,3,2.0),
        (2,4,2.5),
        (3,4,1.0),
        (4,5,3.0)
    ]
    for u_id, v_id, w in edges:
        g.add_edge(id_to_index[u_id], id_to_index[v_id], w)

    start_idx = id_to_index[1]  # Admin (id=1)
    bfs_order_idx = g.bfs(start_idx)
    dfs_order_idx = g.dfs(start_idx)
    print('\nGraph BFS order (building IDs):', [index_to_id[i] for i in bfs_order_idx])
    print('Graph DFS order (building IDs):', [index_to_id[i] for i in dfs_order_idx])

    # Dijkstra
    dist, parent = g.dijkstra(start_idx)
    print('\nDijkstra distances (from Admin id=1):')
    for i,d in enumerate(dist):
        print(f'  to {index_to_id[i]}: {d}')

    # Reconstruct path to Gym (id=5)
    target = id_to_index[5]
    path = []
    cur = target
    while cur is not None:
        path.append(index_to_id[cur])
        cur = parent[cur]
    path.reverse()
    print('Shortest path to Gym (ids):', path)

    # Kruskal
    mst_w, mst_edges = g.kruskal_mst()
    print('\nKruskal MST total weight:', mst_w)
    print('MST edges (u_id, v_id, weight):')
    for u,v,w in mst_edges:
        print(' ', index_to_id[u], index_to_id[v], w)

    # Expression tree
    tokens = ['3','4','+','2','*','7','/']  # postfix
    et = ExpressionTree()
    et.build_from_postfix(tokens)
    val = et.evaluate()
    print('\nExpression Tree: tokens', tokens, '-> value =', val)

    # Search demo
    print('\nSearch BST for Building ID 4:', bst.search(4))
    print('Search BST for Building ID 99 (nonexistent):', bst.search(99))

    print('\n--- Demo finished ---\n')

if __name__ == '__main__':
    demo()
