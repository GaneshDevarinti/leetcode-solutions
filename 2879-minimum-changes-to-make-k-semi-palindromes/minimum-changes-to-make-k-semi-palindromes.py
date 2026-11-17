class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float("inf")

        # Precompute divisors for every possible substring length m (2 <= m <= n)
        divisors = [[] for _ in range(n + 1)]
        for d in range(1, n):
            for m in range(2 * d, n + 1, d):
                divisors[m].append(d)

        # cost[l][r]: min changes to make s[l..r] a semi-palindrome
        cost = [[INF] * n for _ in range(n)]
        for l in range(n):
            for r in range(l + 1, n):
                m = r - l + 1
                best = INF
                for d in divisors[m]:
                    grp_len = m // d
                    changes = 0
                    for rem in range(d):
                        for p in range(grp_len // 2):
                            left_idx = l + rem + p * d
                            right_idx = l + rem + (grp_len - 1 - p) * d
                            if s[left_idx] != s[right_idx]:
                                changes += 1
                    if changes < best:
                        best = changes
                cost[l][r] = best

        # dp[i][parts]: min changes to partition s[:i] into `parts` semi-palindromes
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for parts in range(1, k + 1):
            for i in range(2 * parts, n + 1):
                for j in range(2 * (parts - 1), i - 1):
                    val = dp[j][parts - 1] + cost[j][i - 1]
                    if val < dp[i][parts]:
                        dp[i][parts] = val

        return dp[n][k]
