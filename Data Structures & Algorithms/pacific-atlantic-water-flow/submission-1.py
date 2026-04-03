class Solution:
    def check(self, r, c, heights, grid):
        grid[r][c] = True

        directions = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]

        for dr, dc in directions:
            if 0 <= dr < len(heights) and 0 <= dc < len(heights[0]) and not grid[dr][dc] and heights[r][c] <= heights[dr][dc]:
                self.check(dr, dc, heights, grid)
        
        return
        
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        res = []
        atlantic_grid = [[False] * n for _ in range(m)]
        pacific_grid = [[False] * n for _ in range(m)]

        # iterate over up & bottom row in heights grid
        for i in range(n):
            self.check(0, i, heights, pacific_grid)
            self.check(m - 1, i, heights, atlantic_grid)
        
        # iterate over left and right row in heights grid
        for j in range(m):
            self.check(j, 0, heights, pacific_grid)
            self.check(j, n - 1, heights, atlantic_grid)

        for i in range(m):
            for j in range(n):
                if pacific_grid[i][j] and atlantic_grid[i][j]:
                    res.append([i, j])
        
        return res




        


    
        