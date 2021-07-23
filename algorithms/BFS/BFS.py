from typing import Dict, Optional, List


class Graph:

    def __init__(self, directive=False):
        self.directive = directive
        self.number_of_nodes = 0
        self.nodes: Dict[str, set] = {}

    def __repr__(self):
        txt = 'DrcG' if self.directive else 'NonDG'
        return txt + str(self.number_of_nodes)

    def __getitem__(self, item):
        return self.nodes[item]

    def add_node(self, name: str):
        if name in self.nodes:
            print(f'"{name}" node previously added')
        else:
            self.nodes[name] = set()
            self.number_of_nodes += 1

    def add_edge_and_node(self, source: str, sink: str):
        if source not in self.nodes:
            self.add_node(source)
        if sink not in self.nodes:
            self.add_node(sink)
        self.nodes[source].add(sink)
        if not self.directive:
            self.nodes[sink].add(source)

    def add_multi_sink(self, source: str, *args: str):
        for sink in args:
            self.add_edge_and_node(source, sink)


def bfs(base_graph: Graph, node_base: str, goal_node: Optional[str] = None) -> List:
    discovered = [node_base]
    queue = list(base_graph[node_base])
    while queue:
        vertex = queue.pop(0)
        if vertex == goal_node:
            discovered.append(vertex)
            return discovered
        elif vertex not in discovered:
            discovered.append(vertex)
            queue.extend(list(base_graph[vertex]))
    return discovered


if __name__ == '__main__':
    graph = Graph(directive=True)
    graph.add_multi_sink('A', 'B', 'C')
    graph.add_edge_and_node('B', 'D')
    graph.add_edge_and_node('B', 'E')
    graph.add_edge_and_node('D', 'E')
    graph.add_edge_and_node('C', 'D')
    print(bfs(graph, 'A'))
