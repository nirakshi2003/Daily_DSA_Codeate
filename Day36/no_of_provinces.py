def take_input():
  n=int(input("Enter the number of nodes: "))
  m=int(input("Enter the number of edges: "))
  graph=[[] for _ in range(n)]
  for i in range(m):
    u, v=map(int, input(f"Enter edge {i+1} (start end): ").split())
    graph[u].append(v)
    graph[v].append(u)
  return graph

def find_provinces(graph):
  visited=set()
  provinces=0
  
  def dfs(node):
    if node in visited:
      return
    visited.add(node)
    for neighbor in graph[node]:
      dfs(neighbor)
  
  for node in range(len(graph)):
    if node not in visited:
      provinces += 1
      dfs(node)
  return provinces

graph=take_input()

print(find_provinces(graph))
