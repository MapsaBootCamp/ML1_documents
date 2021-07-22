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


def dfs(base_graph: Graph, node_base: str, discovered: Optional[List] = None) -> List:
    if discovered is None:
        discovered = [node_base]
    else:
        discovered.append(node_base)
    for node in base_graph[node_base]:
        if node not in discovered:
            dfs(base_graph, node, discovered)
    return discovered


if __name__ == '__main__':
    graph = Graph(directive=True)
    graph.add_multi_sink('A', 'B', 'C')
    graph.add_edge_and_node('B', 'D')
    graph.add_edge_and_node('B', 'E')
    graph.add_edge_and_node('D', 'E')
    graph.add_edge_and_node('C', 'D')
    print(dfs(graph, 'A'))
