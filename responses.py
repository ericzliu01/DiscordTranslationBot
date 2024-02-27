import minesweeper_test

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'glape'
    
    if p_message == 'minesweeper': 
        board = minesweeper_test.generate_minesweeper_board(10, 0.2)
        message = ""
        for i in range(10): # 10 is just arbitrary length, make var
            for j in range(10):
                message += f"||:{sweeper_num_converter(board[i][j])}:||"
                # message += str(board[i][j])
            message += '\n'
        return message

def sweeper_num_converter(num):
    if num == 0:
        return 'zero'
    elif num == 1:
        return 'one'
    elif num == 2:
        return 'two'
    elif num == 3:
        return 'three'
    elif num == 4:
        return 'four'
    elif num == 5:
        return 'five'
    elif num == 6:
        return 'six'
    elif num == 7:
        return 'seven'
    elif num == 8:
        return 'eight'
    else:
        return 'bomb'
# import date & time for fake wordle generator