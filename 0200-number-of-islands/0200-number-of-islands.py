class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        n = len(grid)
        m = len(grid[0])
        count = 0

        # DFS function
        def dfs(r, c):
            if r < 0 or c < 0 or r >= n or c >= m or grid[r][c] != '1':
                return
            
            grid[r][c] = '0'  # mark visited

            # Explore 4 directions
            dfs(r-1, c)  # up
            dfs(r+1, c)  # down
            dfs(r, c-1)  # left
            dfs(r, c+1)  # right

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)

        return count