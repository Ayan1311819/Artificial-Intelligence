# DFS
1. Start with a frontier that contains initial state
2. Start with an empty explored set
3. Repeat
  > If the frontier is empty, then no solution
  > Remove a node from the frontier ()
  > If node contains goal state, return the solution
  > Add node to the explored set
  > Expand node(), add resulting nodes to the frontier if they aren't already in the frontier or the explored set