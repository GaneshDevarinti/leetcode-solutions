import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        # Step 1: Build the adjacency list for the directed weighted graph
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]
        
        # Min-heap elements: (current_distance, current_node, consecutive_count)
        # Starting at node 0 initializes a running streak of 1 identical character.
        pq = [(0, 0, 1)]
        dist[0][1] = 0
        
        while pq:
            d, u, c = heapq.heappop(pq)
            
            # If we found a strictly shorter path to this specific state already, skip it
            if d > dist[u][c]:
                continue
                
            # Dijkstra pops the overall closest state first. 
            # Reaching n - 1 guarantees the shortest path.
            if u == n - 1:
                return d
                
            # Traverse outgoing connections
            for v, wt in adj[u]:
                # Increment the identical character streak if labels match, otherwise reset to 1
                next_count = c + 1 if labels[v] == labels[u] else 1
                
                # Prune transitions that violate the max-k run rule
                if next_count > k:
                    continue
                    
                # Standard relaxation step
                if d + wt < dist[v][next_count]:
                    dist[v][next_count] = d + wt
                    heapq.heappush(pq, (d + wt, v, next_count))
                    
        return -1
