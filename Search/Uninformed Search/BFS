class Graph:
    def __init__(self):
        self.graph = {} #dictionary 
    
    def add_edge(self,u,v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v) # looks like this  'B': ['A', 'D']

    def dfs(self, start_node, goal):
        frontier=[start_node] #initializing the frontier
        explored = []
        while frontier:
            current_node = frontier.pop(0) #Since you are using a queue so you will be popping the first element of the frontier (FIFO)
            if(current_node==goal):
                print(current_node)
                return True
            if current_node not in explored:
                explored.append(current_node)
                print(current_node,end="--> ") #BFS traversal
            else:
                continue
            if current_node in self.graph:
                for neighbours in self.graph[current_node]:
                    if neighbours not in explored:
                       frontier.append(neighbours)


if __name__ == "__main__":
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(3, 6)
    g.add_edge(2, 8)
    print("|| BFS traversal ||")
    g.dfs(1,8)
