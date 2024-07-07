class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))
    
    def get_neighbors(self, u):
        return [v for v, _ in self.graph.get(u, [])]
    
    def ucs(self, start_node, goal):
        frontier = [(start_node,0)]
        explored = set()
        
        while frontier:
            current_node, current_cost = frontier.pop(0)
            if current_node == goal:
                print(current_node)
                return True
            
            if current_node not in explored:
                explored.add(current_node)
                print(current_node,end="-->")
                
                for neighbor, weight in self.graph.get(current_node, []):
                    new_cost = current_cost + weight
                    if neighbor not in explored:
                        frontier.append((neighbor,new_cost))
                        frontier.sort(key=lambda x: x[1])
        print("Goal not found")

# Example usage:
if __name__ == "__main__":
    g = Graph()
    g.add_edge("A", "B", 5)
    g.add_edge("A", "C", 3)
    g.add_edge("B", "C", 2)
    g.add_edge("C", "D", 4)
    print("| Uniform Cost Search Traversal |")
    start_node = "A"
    goal_node = "D"
    g.ucs(start_node, goal_node)
