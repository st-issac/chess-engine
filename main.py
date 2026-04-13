# This is the main file for the chess engine. It will hold the class definitions
# for the board and pieces, as well as the move generation and evaluation functions. 

class Board:
    def __init__(self):
        # Holds the attributes for the methods used within the class definition
        row_dim, col_dim = 8, 8
        
        grid = [[0 for _ in range(8)] for _ in range(8)]   

        back_rank = ['r','n','b','q','k','b','n','r']
        pawns = ['p','p','p','p','p','p','p','p']

        grid[0] = back_rank
        grid[1] = pawns
        grid[6] = [item.upper() for item in pawns]
        grid [7] = [item.upper() for item in back_rank]

        self.grid = grid
        self.rows = row_dim
        self.columns = col_dim


    def display(self):
        # Prints out grid in string form (would be acted upon by move generation and such later)        
        display =  [['.' if cell == 0 else cell for cell in row] for row in self.grid]   

        for row in display:
            print(' '.join(row))
        
        
    def get_square(self, row, col):
        # Returns the string for the element of the grid array
        
        
        pass



board = Board()
board.display()