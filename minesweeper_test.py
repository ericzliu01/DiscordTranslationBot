import random
import math

# grid = [n,m]   // initialize all cells to 0
# for k = 1 to number_of_mines
#    get random mine_x and mine_y where grid(mine_x, mine_y) is not a mine
#    for x = -1 to 1
#       for y = -1 to 1
#          if x = 0 and y = 0 then
#             grid[mine_x, mine_y] = -number_of_mines  // negative value = mine
#          else 
#             increment grid[mine_x + x, mine_y + y] by 1

def generate_minesweeper_board(size, mine_density):
    '''
    '''
    board = [[0 for i in range(size)] for j in range(size)]
    minecount = math.floor(size**2 * mine_density)
    planted_mines = 0

    # mine placement
    #while (planted_mines < minecount):

    while planted_mines < minecount:
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        if board[x][y] != '0':
            board[x][y] = 9
            i = x - 1
            while i <= x + 1:
                j = y - 1
                while j <= y + 1:
                    if (not (i < 0 or i == size)) and (not (j < 0 or j == size)):
                        if (board[i][j] != 9):
                            board[i][j] += 1
                    j += 1
                i += 1
                        
            # if x == 0:
            #     x1 = 0
            #     x2 = 1
            # elif x == size - 1:
            #     x1 = size - 2
            #     x2 = size - 1
            # else:
            #     x1 = x - 1
            #     x2 = x + 1
            # if y == 0:
            #     y1 = 0
            #     y2 = 1
            # elif y == size - 1:
            #     y1 = size - 2
            #     y2 = size - 1
            # else:
            #     y1 = y - 1
            #     y2 = y + 1
            # i = x1
            # while i < x2:
            #     j = y1
            #     while j < y2:
            #         if board[i][j] != 9:
            #             board[i][j] += 1
            #         j += 1
            #     i += 1
            planted_mines += 1

    return board
    # print_board(board)
    # print(planted_mines, 'mines planted')

def find_neighbors(x, y, size):
    return

def print_board(board):
    for i in range(len(board)):
        print(board[i])

def discord_to_string(board): 
    result = ''
    for i in range(len(board)):
        for j in range(len(board[i])):
            result += board[i][j]
        result += '\n'
    return result

print_board(generate_minesweeper_board(10, 0.2))