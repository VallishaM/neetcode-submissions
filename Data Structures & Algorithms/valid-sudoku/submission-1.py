class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #Checking rows for duplicates
        for i in range(9):
            row_mem = set()
            column_mem = set()
            for j in range(9):
                if board[i][j] in row_mem:
                    return False
                if board[i][j] !='.':
                    row_mem.add(board[i][j])
                if board[j][i] in column_mem:
                    return False
                if board[j][i] !='.':
                    column_mem.add(board[j][i])
        
        #Checking the boxes for duplicates

        for r in range(0, 3):
            for c in range(0, 3):
                
                mem = set()
                for i in range(r*3, r*3+3, 1):
                    for j in range(c*3, c*3+3,1):
                        
                        if board[i][j] in mem:
                            return False
                        if board[i][j]!='.':
                            mem.add(board[i][j])
        return True