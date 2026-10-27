class Solution:
  def createGrid(self, m: int, n: int) -> list[str]:
    # Initialize grid filled with obstacles ('#')
    g = [["#"] * n for _ in range(m)]

    # Make the first row free
    g[0] = ["."] * n

    # Make the last column free
    for i in range(m):
      g[i][-1] = "."

    return ["".join(row) for row in g]
