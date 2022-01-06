class Node:

    number = 0
    nodes = []
    check = False
    connections = {}

    def __init__(self, number):
        self.number = number
        self.nodes = []
    
    def join(self, other, weigth ):
        if(self not in other.nodes and other not in self.nodes):
            self.nodes.append(other)
            other.nodes.append(self)

        if Node.connections.get(self) != None:
          Node.connections[self].update([(other, weigth)])
        else:
          Node.connections[self]={other: weigth}

        if Node.connections.get(other) != None:
          Node.connections[other].update([(self, weigth)])
        else:
          Node.connections[other]={self: weigth}


    def find(self, node, visited = [], check = False):

        Node.check = check
        visited.append(self)
        if(node in self.nodes):
            Node.check = True
        else:
            for other in self.nodes:
                if other not in visited:
                    other.find(node, visited,Node.check )

        return Node.check
      
    def print(self):
        print(self.nodes)

    def printAll(self):
        print(Node.connections)

    def __repr__(self):
        return str(self.number)

    @staticmethod  
    def matrix():
      N = [[0]*len(Node.connections) for i in range(len(Node.connections))]
      for i in Node.connections:
         for j in Node.connections.get(i):
           N[i.number][j.number]= int(Node.connections.get(i).get(j))
      for i in range(0, len(N)):
        for i2 in range(0, len(N[i])):
          print(N[i][i2], end=' ')
        print()
      return N


    @staticmethod
    def dijkstra(src):
        graph = Node.matrix()
        visited = []
        distance = {src: 0}
        node = list(range(len(graph[0])))
        if src in node:
            node.remove(src)
            visited.append(src)
        else:
            return None
        for i in node:
            distance[i] = graph[src][i]
        prefer = src
        while node:
            _distance = float('inf')
            for i in visited:
                for j in node:
                    if graph[i][j] > 0:
                        if _distance > distance[i] + graph[i][j]:
                            _distance = distance[j] = distance[i] + graph[i][j]
                            prefer = j
            visited.append(prefer)
            node.remove(prefer)
        return distance

a = Node(0)
b = Node(1)
c = Node(2)
d = Node(3)
e = Node(4)
f = Node(5)
#Второй элемент - расстояние
a.join(b, 2)
b.join(c, 3)
c.join(a,5)
d.join(b,7)
e.join(d, 8)

print("Поиск в глубину, узел в графе ")
print(a.find(e))
print("Поиск в глубину, узел вне графа")
print(a.find(f))

print("Связи узла a ")
a.print()
print("====================")
print("Связи всех узлов и из вес ")
a.printAll()
print("====================")
print("Матрица смежности и алгоритм Дейкстры(сам алгоритм немного позаимствован), кратчайшие пути первого элемента до остальных")
da = a.dijkstra(0)

print(da)




