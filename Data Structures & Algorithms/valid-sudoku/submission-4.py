class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        square_mem=[set() for _ in range(9)]
         
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
                
                square_number = i//3 * 3 + j//3
                
                if board[i][j] in square_mem[square_number]:
                    return False
                if board[i][j] != '.':
                    square_mem[square_number].add(board[i][j])
        
        return True