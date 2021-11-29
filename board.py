def print_board():
    for lst in board:
        print(lst)
       
def check_win():
    #check rows for win
    if lst1[0] == lst1[1] == lst1[2] and lst1[0] != "-":
        print("Player number", player_num, "wins!")
        game_over()
    elif lst2[0] == lst2[1] == lst2[2] and lst2[0] != "-":
        print("Player number", player_num, "wins!")
        game_over()        
    elif lst3[0] == lst3[1] == lst3[2] and lst3[0] != "-":
        print("Player number", player_num, "wins!")
        game_over()
    #check columns for win
    elif lst1[0] == lst2[0] == lst3[0] and lst1[0] != "-":
        print("Player number", player_num, "wins!")
        game_over()
    elif lst1[1] == lst2[1] == lst3[1] and lst1[1] != "-":
        print("Player number", player_num, "wins!")
        game_over()
    elif lst1[2] == lst2[2] == lst3[2] and lst1[2] != "-":
        print("Player number", player_num, "wins!")
        game_over()
    #check diagonals for win
    elif lst1[0] == lst2[1] == lst3[2] and lst1[0] != "-":
        print("Player number", player_num, "wins!")
        game_over()
    elif lst1[2] == lst2[1] == lst3[0] and lst1[2] != "-":
        print("Player number", player_num, "wins!")
        game_over()
    else:
        pass

def mark_board(player):
    
    played = 0
    
    while played == 0:
        
        print("Player number",player,"please make your move.")
        
        while True:
            try: 
                column_num = int(input("Please enter a column number (1-3):"))
            except ValueError:
                print("Invalid entry.") # message about not an integer
                continue
            if 1 <= column_num <= 3:
                break
            print("Please enter a column number between 1 and 3")
            
        while True:
            try: 
                row_num = int(input("Please enter a row number (1-3):"))
            except ValueError:
                print("Invalid entry.") # message about not an integer
                continue
            if 1 <= row_num <= 3:
                break
            print("Invalid entry") 

        for index, lst in enumerate(board):
            if index == row_num - 1:
                if lst[column_num-1] == "-":
                    if player == 1:                        
                        lst[column_num-1] = "X"
                        played = 1
                        print_board()
                        check_win()
                        
                    else:
                        lst[column_num-1] = "0"
                        played = 1
                        print_board()
                        check_win()
                        
            
                else:
                    print("Space is already taken. Please play again")
                    
    #return player

def game_over():
    print("Thank you for playing tic tac toe!")
    gameover = 1
    quit()
    
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
    

        

   




