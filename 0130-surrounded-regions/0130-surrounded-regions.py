from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        
        n, m = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or r >= n or c < 0 or c >= m or board[r][c] != 'O':
                return
            
            board[r][c] = '#'

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

         
        for i in range(n):
            dfs(i, 0)
            dfs(i, m-1)

         
        for j in range(m):
            dfs(0, j)
            dfs(n-1, j)

        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
        