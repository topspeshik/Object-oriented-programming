from collections import deque


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

        if Node.connections.get(self.number) != None:
          Node.connections[self.number].update([(other.number, weigth)])
        else:
          Node.connections[self.number]={other.number: weigth}

        if Node.connections.get(other.number) != None:
          Node.connections[other.number].update([(self.number, weigth)])
        else:
          Node.connections[other.number]={self.number: weigth}


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
    def dijkstra(start):
        G = Node.connections
        Q = deque()
        S ={}
        S[start] = 0
        Q.append(start)
        while Q:
          cur = Q.popleft()
          for u in G[cur]:
            if (u not in S) or (S[cur] + G[cur][u] < S[u]):
              S[u] = S[cur] + G[cur][u]
              Q.append(u)
        return S

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
print("Связи всех узлов и их вес ")
a.printAll()
print("====================")
print("Алгоритм Дейкстры через очередь")
S = a.dijkstra(0)

print(S)



