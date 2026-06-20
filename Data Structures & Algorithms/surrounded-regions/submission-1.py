from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def bfs(r: int, c: int) -> None:
            queue = deque([(r, c)])
            board[r][c] = "T"

            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == "O":
                        board[nx][ny] = "T"
                        queue.append((nx, ny))

        for r in range(rows):
            if board[r][0] == "O":
                bfs(r, 0)
            if board[r][cols - 1] == "O":
                bfs(r, cols - 1)

        for c in range(cols):
            if board[0][c] == "O":
                bfs(0, c)
            if board[rows - 1][c] == "O":
                bfs(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"