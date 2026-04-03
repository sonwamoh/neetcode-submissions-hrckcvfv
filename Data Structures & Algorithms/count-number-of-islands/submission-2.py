class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # solve it using both dfs & bfs
        m, n = len(grid), len(grid[0])

        num_islands = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != '1':
                return 
            
            grid[i][j] = '0'

            dfs(i, j + 1)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i - 1, j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    num_islands += 1
        
        return num_islands



        