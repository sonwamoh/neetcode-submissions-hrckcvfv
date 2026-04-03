class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(r, c, visited):
            ROWS, COLS = m, n
        
            if(max (r, c) < 0 or r == ROWS or c == COLS or (r, c) in visited):
                return 0
        
            if(r == ROWS - 1 and c == COLS - 1):
                return 1
            
            visited.add((r, c))

            count = 0

            count += dfs(r + 1, c, visited)
            count += dfs(r, c + 1, visited)

            visited.remove((r, c))

            return count
        
        return dfs(0, 0, set())

        