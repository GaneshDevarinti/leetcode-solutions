import heapq
class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        n, m = len(servers), len(tasks)
        ans = [0] * m
        # Min-heap for free servers: (weight, index)
        free = [(servers[i], i) for i in range(n)]
        heapq.heapify(free)
        # Min-heap for busy servers: (free_time, weight, index)
        busy = []
        t = 0
        for j in range(m):
            t = max(t, j)
            
            # Release all servers that finish by time t
            while busy and busy[0][0] <= t:
                free_time, weight, idx = heapq.heappop(busy)
                heapq.heappush(free, (weight, idx)) 
            # If no servers are free, advance time to the earliest completion
            if not free:
                t = busy[0][0]
                while busy and busy[0][0] <= t:
                    free_time, weight, idx = heapq.heappop(busy)
                    heapq.heappush(free, (weight, idx))          
            # Assign task j to the available server with smallest weight/index
            weight, idx = heapq.heappop(free)
            ans[j] = idx
            heapq.heappush(busy, (t + tasks[j], weight, idx))
        return ans
