class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def get_edges(self, u):
        return self.graph.get(u, [])


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(21, 7)
    graph.add_edge(21, 20)
    graph.add_edge(7, 20)

    print(graph.get_edges(21))
    print(graph.get_edges(7))
