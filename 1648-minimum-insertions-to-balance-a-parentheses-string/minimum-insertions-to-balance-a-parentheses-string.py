class Solution:

  def minInsertions(self, s: str) -> int:
    res = 0
    need = 0
    i = 0
    n = len(s)
    
    while i < n:
      if s[i] == "(":
        need += 2
        if need % 2 != 0:
          res += 1
          need -= 1
      else:
        need -= 1
        if need < 0:
          res += 1
          need += 2
      i += 1

    return res + need
