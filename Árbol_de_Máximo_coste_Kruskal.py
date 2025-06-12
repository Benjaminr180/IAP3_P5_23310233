class UnionFind:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # compresión de camino
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            self.parent[root2] = root1
            return True
        return False


def kruskal_max_tree(nodes, edges):
    uf = UnionFind(nodes)
    max_tree = []
    total_cost = 0

    print("\nPaso a paso del algoritmo de Kruskal (máximo costo):\n")
    edges_sorted = sorted(edges, key=lambda x: x[2], reverse=True)  # Orden descendente

    for u, v, weight in edges_sorted:
        print(f"Probando arista ({u}, {v}) con peso {weight}...")
        if uf.union(u, v):
            print(f"Arista ({u}, {v}) agregada al árbol.")
            max_tree.append((u, v, weight))
            total_cost += weight
        else:
            print(f"Arista ({u}, {v}) forma un ciclo. No se agrega.")
        print()

    print("Árbol de máximo costo completo:")
    for u, v, weight in max_tree:
        print(f"{u} - {v} : {weight}")
    print(f"\nCosto total: {total_cost}")


# Datos de prueba
nodos = ['A', 'B', 'C', 'D', 'E']
aristas = [
    ('A', 'B', 1),
    ('A', 'C', 5),
    ('B', 'C', 3),
    ('B', 'D', 4),
    ('C', 'D', 2),
    ('C', 'E', 6),
    ('D', 'E', 7)
]

kruskal_max_tree(nodos, aristas)
