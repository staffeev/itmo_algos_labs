class Solution:
    """https://leetcode.com/problems/surrounded-regions/description/"""
    def solve(self, board: list[list[str]]) -> None:
        n, m = len(board), len(board[0])

        def dfs(x, y):
            board[x][y] = "0"
            if x > 0 and board[x - 1][y] == "O":
                dfs(x - 1, y)
            if x < n - 1 and board[x + 1][y] == "O":
                dfs(x + 1, y)
            if y > 0 and board[x][y - 1] == "O":
                dfs(x, y - 1)
            if y < m - 1 and board[x][y + 1] == "O":
                dfs(x, y + 1)

        for j in range(m):
            if board[0][j] == "O":
                dfs(0, j)
            if board[n - 1][j] == "O":
                dfs(n - 1, j)
        for i in range(1, n - 1):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][m - 1] == "O":
                dfs(i, m - 1)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "0":
                    board[i][j] = "O"


if __name__ == "__main__":
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    s = Solution()
    s.solve(board)
    for i in board:
        print(*i)