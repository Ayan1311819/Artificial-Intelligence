*.py linguist-language=Python
class Graph:
    def __init__(self):
        self.graph = {} #dictionary 
    
    def add_edge(self,u,v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v) # looks like this  'B': ['A', 'D']

    def dfs(self, start_node, goal):
        frontier=[start_node] #initializing the frontier
        explored = set()
        optimal_path = []
        while frontier:
            current_node=frontier.pop() # Pop the last node from frontier
            optimal_path.append(current_node)
            print("Optimal path",optimal_path)
            if(not self.graph.get(current_node) ) and current_node != goal:
                optimal_path.pop()
            #Goal Test
            if(current_node==goal):
                optimal_path.append(current_node)
                return True
            if current_node not in explored:
                explored.add(current_node)
                #print(current_node) #DFS traversal 
            else:
                continue
            if current_node in self.graph:
                for neighbours in self.graph[current_node]:
                    if neighbours not in explored:
                       frontier.append(neighbours)#frontier.extend(self.graph[current_node]) # Add all the neighbors of current node to frontier
            

        
if __name__ == "__main__":
    g=Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(3, 6)
    g.add_edge(2, 8)
    print("|| DFS traversal ||")
    g.dfs(1,8)
