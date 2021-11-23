def print_board():
    lst1 = ['-','-','-']
    lst2 = ['-','-','-']
    lst3 = ['-','-','-']
    board = [lst1, lst2, lst3]
    for lst in board:
        print(lst)

def mark_board():
    print("Player number one, please make your move:")
    column_num = int(input("Please enter the column number (1-3):"))
    while column_num < 1 or column_num > 3:
        column_num = int(input("Please enter a valid column number (1-3):"))
    row_num = int(input("Please enter the row number (1-3):"))
    while row_num < 1 or row_num > 3:
        row_num = int(input("Please enter a valid column number (1-3):"))

    lst1 = ['-','-','-']
    lst2 = ['-','-','-']
    lst3 = ['-','-','-']
    board = [lst1, lst2, lst3]

    for index, lst in enumerate(board):
        if index == row_num - 1:
            lst[column_num-1] = "X"

    for x in board:
        print(x)

print_board()
mark_board()

