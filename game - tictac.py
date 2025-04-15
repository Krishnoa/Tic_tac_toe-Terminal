import itertools

def game_board(game_map,player=0,row=0,colum=0,Display=False,):
    # game_map takes game i.e nested list we made
    try: 
        if game_map[row][colum] != 0:
            print(f"This postion is Played by {game_map[row][colum]}, TRY AGAIN!!")
            return game_map,False   
        if Display == False:# if somebody played we change the value at row and col
            game_map[row][colum] = player
        print(" 0, 1, 2 ")
        for i,x in enumerate(game_map):
            print(x,i)
        return game_map,True # stores the changed output - because of that tempary variable this funcation becomes powerfull enough to take any value store that value it is reusable thing 
    except Exception as e:
            print(e) # curently we dont need just for show
            return game_map,False   


#Winning condtion - hr win , Vr win , D win
def win(Current_game):
     for row in game: # Horizontal win!
          if row.count(row[0])==len(row) and row[0] != 0:
              print(f"Player {row[0]} has Won - Horzontally(--)")
              return False    
       # vertical Win!!     
     for cols in range(len(game)):
        col=[]
        for row in game: 
            col.append(row[cols])
        if col.count(col[0]) == len(col) and col[0] != 0 :
              print(f"Player {col[0]} has Won - Verticaly(|)")
              return False
        #Diganals
     Ds2=[]
     for i,d in enumerate(reversed(range(len(game)))):
      Ds2.append(game[i][d])
     if Ds2.count(Ds2[0]) == len(Ds2) and Ds2[0] != 0:
      print(f"Player {Ds2[0]} has Won - Digonally(/)")
      return False
     
     Ds1 = []
     for d in range(len(game)):
      Ds1.append(game[d][d])
     if Ds1.count(Ds1[0]) == len(Ds1) and Ds1[0] != 0:
      print(f"Player {Ds1[0]} has Won - Digonally(\\)")
      return False
     return True


play = True
while play :
    player = itertools.cycle([1,2])
    game = [[0,0,0],   # it for Because for restarting the game you - Game starts at Evert
            [0,0,0],
            [0,0,0]]
    game, _ = game_board(game,Display = True)
    game_won = False
    
    while not game_won:
        Current_player = next(player)
        print(f"Current Player : {Current_player}")
        played = False
        
        while played == False:
            Row_choice = int(input("Enter the row you want to select(0,1,2) "))
            Colum_choice = int(input("Enter the Col you want to select(0,1,2) "))
            game,played = game_board(game,Current_player,Row_choice,Colum_choice)
        
        if win(game) == False:
            game_won = True
            play_again = input( " WOULD YOU LIKE TO PLAY AGAIN (y/n)?? ")
            if play_again.lower() == "y" :
                print("Restarting.......")
            elif play_again.lower() == "n":
                print("Thankyou!!Byeeee")
                play = False
            else:
                print (" you entered something esle!! Bye")
                play = False    
        


        
