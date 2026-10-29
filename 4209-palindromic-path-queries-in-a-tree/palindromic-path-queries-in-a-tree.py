import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(300000)

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # Binary lifting & Euler tour variables
        LOGN = 17  # Since n <= 5 * 10^4, 2^16 = 65536
        up = [[0] * LOGN for _ in range(n)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 1
        
        # Iterative DFS to avoid deep recursion limits if preferred, 
        # but structured cleanly here via a simulated stack.
        stack = [(0, -1, False)]  # (node, parent, is_processed)
        tour_order = []
        
        # standard DFS for tree properties
        visited = [False] * n
        parent_map = [-1] * n
        dep = [0] * n
        
        # Re-constructing step using standard iterative DFS
        dfs_stack = [0]
        visited[0] = True
        order = []
        
        while dfs_stack:
            curr = dfs_stack.pop()
            order.append(curr)
            for neighbor in adj[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent_map[neighbor] = curr
                    dep[neighbor] = dep[curr] + 1
                    dfs_stack.append(neighbor)
                    
        # Compute Binary Lifting Table
        for v in range(n):
            up[v][0] = parent_map[v] if parent_map[v] != -1 else 0
            depth[v] = dep[v]
            
        for j in range(1, LOGN):
            for i in range(n):
                up[i][j] = up[up[i][j-1]][j-1]
                
        # Compute tin and tout using the order
        # We can simulate the timing tracking entry and exit
        # A simpler way to get tin/tout ranges for subtree updates:
        tin = [0] * n
        tout = [0] * n
        t = 1
        
        # Post-order tracking for exact subtree ranges
        adj_forward = [[] for _ in range(n)]
        for i in range(1, n):
            adj_forward[parent_map[i]].append(i)
            
        dfs_stack = [(0, 0)]  # (node, state: 0=enter, 1=exit)
        while dfs_stack:
            curr, state = dfs_stack.pop()
            if state == 0:
                tin[curr] = t
                t += 1
                dfs_stack.append((curr, 1))
                for child in adj_forward[curr]:
                    dfs_stack.append((child, 0))
            else:
                tout[curr] = t
                t += 1

        # Fenwick Tree (Binary Indexed Tree) for range XOR updates
        # Size needs to handle up to max value of t (which is 2*n + 1)
        BIT_SIZE = t + 2
        bit = [0] * BIT_SIZE
        
        def bit_update(idx, val):
            while idx < BIT_SIZE:
                bit[idx] ^= val
                idx += idx & (-idx)
                
        def bit_query(idx):
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res
            
        def update_node_mask(u, old_char, new_char):
            old_mask = 1 << (ord(old_char) - 97)
            new_mask = 1 << (ord(new_char) - 97)
            xor_diff = old_mask ^ new_mask
            # Apply xor_diff to u's entire subtree
            bit_update(tin[u], xor_diff)
            bit_update(tout[u], xor_diff)

        # LCA Query Function
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for j in range(LOGN):
                if (diff >> j) & 1:
                    u = up[u][j]
            if u == v:
                return u
            for j in range(LOGN - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
            return up[u][0]

        # Initialize current string and node masks into Fenwick Tree
        current_chars = list(s)
        for i in range(n):
            mask = 1 << (ord(current_chars[i]) - 97)
            bit_update(tin[i], mask)
            bit_update(tout[i], mask)
            
        # Process Queries
        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                update_node_mask(u, current_chars[u], c)
                current_chars[u] = c
            else:
                u = int(parts[1])
                v = int(parts[2])
                lca = get_lca(u, v)
                
                # Query paths from root to u, root to v
                mask_u = bit_query(tin[u])
                mask_v = bit_query(tin[v])
                mask_lca_char = 1 << (ord(current_chars[lca]) - 97)
                
                # Total path mask compilation
                path_mask = mask_u ^ mask_v ^ mask_lca_char
                
                # Verify palindrome configuration (at most 1 bit set)
                is_palindrome = (path_mask & (path_mask - 1)) == 0
                ans.append(is_palindrome)
                
        return ans
