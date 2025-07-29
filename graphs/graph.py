# Different types of graphs we could implement.
# Edge list: Where each vertex is connected by an edge
graph1 = [[0, 1], [1, 2], [3, 1], [0, 3]]

# Adjacent List: The index is the vertex and the value is the vertex neighbors
graph2 = [[2], [2, 3], [0, 1, 3], [1, 2]]

# Adjacent Matrix: 0 and 1 to indicate if the x and y have a connection to the vertex
graph3 = [
    [0, 1, 0 ,0],
    [1, 0, 1, 1],
    [0, 1, 1, 0],
    [0, 0, 0, 1],
]

# Implementing a Graph class using adajency lists.
class Graph:
    def __init__(self, directed=False):
        # Using dictionaries to store graph, also creating a check to see if the graph is directred, set to false
        self.adjlist = {}
        self.directed = directed

    def addVertex(self, node):
        # Quite simple, if the vertex is not in the graph add it, initialized with an empty list to hold neighbors
        if node not in self.adjlist:
            self.adjlist[node] = [] 
    
    def addEdge(self, node1, node2):
        # Making sure that both nodes are in the graph as Vertices
        self.addVertex(node1)
        self.addVertex(node2)
        # Adding Node2 to Node1 list: node1 -> node2
        self.adjlist[node1].append(node2)
        # If undirected it also connects the other way: node 1 <- node2
        if not self.directed:
            self.adjlist[node2].append(node1)

    def removeVertex(self, node):
        # Checks to see if the vertex is in the list
        if node in self.adjlist:
            # loop through all neighbors and remove it from their lists
            for neighbor in self.adjlist[node]:
                self.adjlist[neighbor].remove(node)
            # delete vertex its self
            del self.adjlist[node]
        # If graph is directed, remove any incoming edges to that vertex
        if self.directed:
            for v in self.adjlist:
                if node in self.adjlist[v]:
                    self.adjlist[v].remove(node)

    def removeEdge(self, node1, node2):
        # Checks to see if the edge exists to avoid errors
        # Removes the connection from node1 -> node2
        if node1 in self.adjlist and node2 in self.adjlist[node1]:
            self.adjlist[node1].remove(node2)
        # If undirected, removes connection from node1 <- node2
        if not self.directed and node2 in self.adjlist and node1 in self.adjlist[node2]:
            self.adjlist[node2].remove(node1)

    # Prints each vertex and the list of its neighbors
    def showConnections(self):
        for vertex in self.adjlist:
            print(f"{vertex}: {self.adjlist[vertex]}")

myGraph = Graph()
myGraph.addEdge("a", "b")
myGraph.addEdge("a", "c")
myGraph.showConnections()