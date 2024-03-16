def shortest_path(edges, n, src):
  dist=[float('inf')] * n
  dist[src]=0
  queue=[]
  queue.append(src)
  while queue:
    u=queue.pop(0)
    for v in edges[u]:
      if dist[v]>dist[u]+1:
        dist[v]=dist[u]+1
        queue.append(v)
  return dist

def take_input():
  n=int(input("Enter the number of nodes: "))
  m=int(input("Enter the number of edges: "))
  edges=[[] for _ in range(n)]
  for i in range(m):
    u, v=map(int, input(f"Enter edge {i+1} (start end): ").split())
    edges[u].append(v)
    edges[v].append(u)
  return n, edges

n, edges=take_input()
src=0

dist=shortest_path(edges, n, src)
print(dist)
