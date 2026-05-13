class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_len = len(board)
        col_len = len(board[0])
        # row
        for i in range(row_len):
            row_set = set()
            for j in range(col_len):
                num = board[i][j]
                if num.isdigit():
                    if num not in row_set:
                        row_set.add(num)
                    else:
                        return False
        # col 
        for j in range(col_len):
            col_set = set()
            for i in range(row_len):
                num = board[i][j]
                if num.isdigit():
                    if num not in col_set:
                        col_set.add(num)
                    else:
                        return False               
        # square
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square_set = set()
                for inner_i in range(3):
                    for inner_j in range(3):
                        num = board[i + inner_i][j + inner_j]
                        if num.isdigit() and num in square_set:
                            print(i + inner_i)
                            print(j + inner_j)
                            print(num)
                            return False
                        elif num.isdigit():
                            square_set.add(num)

        return True

