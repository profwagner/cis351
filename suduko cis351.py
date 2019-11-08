SIZE = 9 #size of board
SUB = int(SIZE ** 0.5) #size of subboard always equal to square root of size
board = [["_" for x in range(SIZE)] for y in range(SIZE)] #make board of all _

board[1][0]=4
board[2][0]=7
board[4][0]=2
board[1][1]=6
board[5][1]=7
board[0][2]=3
board[2][2]=8
board[3][2]=1
        
board[0][3]=8
board[2][3]=9
board[3][3]=5
board[4][3]=3
board[6][3]=2
board[1][4]=2
board[4][4]=8
board[7][4]=5
board[2][5]=5
board[4][5]=7
board[5][5]=6
board[6][5]=9
board[8][5]=1
board[5][6]=3
board[6][6]=7
board[8][6]=2
board[3][7]=8
board[7][7]=4
board[4][8]=4
board[6][8]=5
board[7][8]=6



def print_board(board):
    """
    Print the board 
    NEED TO FIX LINES!!!
    """
    for y in range(SIZE):
        for x in range(SIZE):
            print (board[y][x]," ", end="")
            if (x % SUB) == SUB - 1:
                print ("| ", end="")
        
        print ()
        if (y % SUB) == SUB - 1:
            for x in range(3*SIZE + (3*SUB) -4):
                print ("=", end="")
            print ()    

def check_row (num, row, board):
    """
    return true if num is in row
    """
    for x in range (SIZE): #loop through each column
        
        if num == board[row][x]:
            return True
    return False #checked and num was not in the given row

def check_col (num, col, board):
    """
    return true if num is in col
    """
    pass



def check_block (num, row, col, board):
    """
    return true in num is in the block
    You might want to find the upper left hand corner of the 
    """
    pass

def check_spot (num, row, col, board):
    """
    returns True if the number is present in the row, column, or subblock
    """
    return check_row (num, row, board) or check_block (num, row, col, board) or \
        check_col (num, col, board)

def solve_spot (row, col, board):
    """
    Solves a board that is compled up to row and column
    Retrurns True if solution found
    False if it needs to backtrack
    """
    if row == SIZE: #We are done! board is filled
        return True
    #The next lines find the row and column of next spot
    next_col = (col + 1) % SIZE
    next_row = row
    if next_col == 0:
        next_row = (row + 1)

    #If the board has an opening we will try the different numbers
    if board[row][col] == "_":
        for num in range (1, SIZE+1): 
            if not check_spot (num, row, col, board):
                board[row][col]=num #try number in spot
                if solve_spot (next_row, next_col, board):
                    return True
        board[row][col]= "_" #need to backtrack
        return False
    return solve_spot (next_row, next_col, board) #Already a number in spot so we go on
            
    
    
    
        
def solve(board):
    """
    calls the solve_spot for the upper left hand corner
    returns True if a solution is possible
    """
    
    return solve_spot (0, 0, board)
    
print_board(board)
if solve(board) == True:
    print ("Solved!")
    print_board(board)
else:
    print ("No solution!")
    
    


