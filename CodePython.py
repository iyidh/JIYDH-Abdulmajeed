from collections import defaultdict

class Graph():
    def __init__(self):
        self.edges = defaultdict(list)
        self.weights = {}
    
    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight


graph = Graph()

node1=input("Enter the node 1: ")
node2=input("Enter the node 2: ")
distance1=int(input("Enter the distance between node 1 and node 2: "))
node3=input("Enter the node 1: ")
node4=input("Enter the node 2: ")
distance2=int(input("Enter the distance between node 1 and node 2: "))
node5=input("Enter the node 1: ")
node6=input("Enter the node 2: ")
distance3=int(input("Enter the distance between node 1 and node 2: "))
node7=input("Enter the node 1: ")
node8=input("Enter the node 2: ")
distance4=int(input("Enter the distance between node 1 and node 2: "))
node9=input("Enter the node 1: ")
node10=input("Enter the node 2: ")
distance5=int(input("Enter the distance between node 1 and node 2: "))
node11=input("Enter the node 1: ")
node12=input("Enter the node 2: ")
distance6=int(input("Enter the distance between node 1 and node 2: "))
node13=input("Enter the node 1: ")
node14=input("Enter the node 2: ")
distance7=int(input("Enter the distance between node 1 and node 2: "))
node15=input("Enter the node 1: ")
node16=input("Enter the node 2: ")
distance8=int(input("Enter the distance between node 1 and node 2: "))

edges = [
    (node1,node2 ,distance1),
    (node3, node4,distance2),
    (node5,node6 ,distance3),
    (node7,node8,distance4),
    (node9,node10 ,distance5),
    (node11, node12,distance6),
    (node13,node14,distance7),
    (node15, node16,distance8),
]
for edge in edges:
    graph.add_edge(*edge)

def dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()
    
    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path

print(dijsktra(graph, 'A', 'H'))
