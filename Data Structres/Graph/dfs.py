class graph:
    def __init__(self,nodes):
        self.adj={}
        self.nodes=nodes
        for i in self.nodes:
            self.adj[i]=[]
    def add(self,a,b):
        self.adj[b].append(a)
        self.adj[a].append(b)
        self.adj[b].sort()
        self.adj[a].sort()
    def print(self):
        for i in self.nodes:
            print(i ,"->",end=" ")
            for j in self.adj[i]:
                print(j,"->",end=" ")
            print("null")
    def add_node(self,node):
        self.nodes.append(node)
        self.adj[node] = []
    def dfsI(self,ver):
        visited={}
        for i in self.adj:
            visited[i] = False
        self.visited=visited
        self.dfs(ver)
        print("null")

    def dfs(self,ver):
        self.visited[ver] = True
        print(ver,end="-")

        for j in self.adj[ver]:
            if self.visited[j]==False:
                self.dfs(j)

nodes=[1,2,3,4,5,6,7,8]
g=graph(nodes)
g.add(2,1)
g.add(4,1)
g.add(3,2)
g.add(4,5)
g.add(6,4)
g.add(6,5)
g.add(5,7)
g.add(6,8)
g.add(7,8)
g.dfsI(7)

