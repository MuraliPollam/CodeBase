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
    def bfs(self):
        visited={}
        parent={}
        que=[]
        for i in self.adj:
            visited[i]=False
            parent[i]=None
        max=len(self.nodes)
        count=0
        s=nodes[0]
        que.append(s)
        visited[s]=True
        while count<max:
            x=que[count]
            count=count+1
            for j in self.adj[x]:
                if visited[j]!=True:
                    visited[j]=True
                    parent[j]=x
                    que.append(j)
            print(x,"->",end="")
        print("null")
    def add_node(self,node):
        self.nodes.append(node)
        self.adj[node] = []


nodes=[1,2,3,4,5,6,7,8]
g=graph(nodes)
g.add(7,8)
g.add(2,1)
g.add(4,1)
g.add(3,2)
g.add(6,4)
g.add(4,5)
g.add(6,5)
g.add(5,7)
g.add(6,8)
g.bfs()

