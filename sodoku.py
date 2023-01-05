
#https://leetcode.com/problems/valid-sudoku/

SAMPLE = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
SAMPLE_TWO = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

def isValidSudoku( board: list[list[str]]) -> bool:
    Ellipsis


    def validate_row( board: list[ list ] ) -> bool: 
        
        for row in board: 

            for char in row: 

                if row.count(char) > 1 and char != ".":
                    return False
            
        print("VALID ROWS")
        return True
    

    def validate_collumn( board: list[ list ] ) -> bool: 

        for indx in range( board.__len__() ) : 
            seen = set()

            for col_indx in range( 9 ): 

                if board[col_indx][indx] in seen:
                    return False
                elif board[col_indx][indx] != ".": 
                    seen.add( board[col_indx][indx] )

        print("VALID COLLUMNS")
        return True
    
    def generate_sub_boxes( board: list[ list] ) -> bool: 
        block_of_three = [ ]

        for row in board: 
            block_of_three.append(row[: 3])
            block_of_three.append(row[3: 6])
            block_of_three.append(row[6 : ])
        
        block_of_nine = [ ]

        for indx in [0,1,2, 9,10,11, 18,19,20]: 
            
            block_of_nine.append( [*block_of_three[indx], *block_of_three[indx + 3], *block_of_three[ indx + 6]] )
        return block_of_nine



    def validate_sub_boxes( board: list[list]) -> bool: 
        
        block_of_nine = generate_sub_boxes( board)

        for block in block_of_nine: 

            items = [ x for x in block if x != "."]

            if items.__len__() != list(set(items)).__len__():
                return False
        return True
    

    return ( validate_collumn(board) and validate_row(board) and validate_sub_boxes(board) )

print( isValidSudoku(SAMPLE_TWO) )