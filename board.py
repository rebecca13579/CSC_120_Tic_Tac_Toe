def print_board():
    for lst in board:
        print(lst)
       
def check_win():
    #check rows for win
    if lst1[0] == lst1[1] == lst1[2] and lst1[0] != "-":
        print("You won!")
        game_over()
    elif lst2[0] == lst2[1] == lst2[2] and lst2[0] != "-":
        print("You won!")
        game_over()        
    elif lst3[0] == lst3[1] == lst3[2] and lst3[0] != "-":
        print("You won!")
        game_over()
    #check columns for win
    elif lst1[0] == lst2[0] == lst3[0] and lst1[0] != "-":
        print("You won!")
        game_over()
    elif lst1[1] == lst2[1] == lst3[1] and lst1[1] != "-":
        print("You won!")
        game_over()
    elif lst1[2] == lst2[2] == lst3[2] and lst1[2] != "-":
        print("You won!")
        game_over()
    #check diagonals for win
    elif lst1[0] == lst2[1] == lst3[2] and lst1[0] != "-":
        print("You won!")
        game_over()
    elif lst1[2] == lst2[1] == lst3[0] and lst1[2] != "-":
        print("You won!")
        game_over()
    else:
        #mark_board(player_num)
        pass

def mark_board(player):
    
    played = 0
    
    while played == 0:
        
        print("Player number",player,"please make your move:")
        column_num = int(input("Please enter the column number (1-3):"))
        while column_num < 1 or column_num > 3:
            column_num = int(input("Please enter a valid column number (1-3):"))
        row_num = int(input("Please enter the row number (1-3):"))
        while row_num < 1 or row_num > 3:
            row_num = int(input("Please enter a valid column number (1-3):"))

        for index, lst in enumerate(board):
            if index == row_num - 1:
                if lst[column_num-1] == "-":
                    if player == 1:                        
                        lst[column_num-1] = "X"
                        played = 1
                        print_board()
                        #player = 2
                        check_win()
                        
                    else:
                        lst[column_num-1] = "0"
                        played = 1
                        print_board()
                        #player = 1
                        check_win()
                        
            
                else:
                    print("Space is already taken. Please play again")
                    
        #print_board()
#        check_win()
        
        #change player 
#         if player == 1:
#             player == 0
#         else:
#             player == 1
    return player

def game_over():
    print("Thank you for playing tic tac toe!")
    gameover == 1
    
lst1 = ['-','-','-']
lst2 = ['-','-','-']
lst3 = ['-','-','-']
board = [lst1, lst2, lst3]
gameover = 0
    
print("Let's play Tic Tac Toe!")
print_board()
player_num = 1

while gameover == 0:
    mark_board(player_num)
    if player_num == 1:
        player_num = 2
    else:
        player_num = 1
    print("Player number is now",player_num,".")
    

        

   




