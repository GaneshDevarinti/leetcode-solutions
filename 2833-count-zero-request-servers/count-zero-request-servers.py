class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        # Sort logs by timestamp
        logs.sort(key=lambda item: item[1])
        
        # Sort queries along with their original indices
        sorted_queries = sorted(enumerate(queries), key=lambda item: item[1])
        
        ans = [0] * len(queries)
        count = {}
        active_servers = 0
        
        i = 0
        j = 0
        
        for orig_idx, q in sorted_queries:
            # Expand window to include logs <= q
            while j < len(logs) and logs[j][1] <= q:
                s_id = logs[j][0]
                if count.get(s_id, 0) == 0:
                    active_servers += 1
                count[s_id] = count.get(s_id, 0) + 1
                j += 1
            
            # Shrink window to exclude logs < q - x
            while i < len(logs) and logs[i][1] < q - x:
                s_id = logs[i][0]
                count[s_id] -= 1
                if count[s_id] == 0:
                    active_servers -= 1
                i += 1
            
            ans[orig_idx] = n - active_servers
            
        return ans
