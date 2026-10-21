class Solution:

  def minOperations(self, s: str) -> int:
    if s == ''.join(sorted(s)):
      return 0

    n = len(s)
    if n == 2:
      return -1

    min_char = min(s)
    max_char = max(s)

    # 1 operation if the min is at the start or max is at the end
    if s[0] == min_char or s[-1] == max_char:
      return 1

    # 2 operations if min or max sits somewhere in the middle
    if min_char in s[1:-1] or max_char in s[1:-1]:
      return 2

    return 3
