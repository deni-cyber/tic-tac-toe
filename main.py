#this is a tic tac toe game


#the current state is a list of lists that can 
#be changed as the game progresses.
#we can address every list in the list as a an
#individual row and every member of the list can
#have their own collumn.
#how do we determine the winner?
# -maybe i could write a function that scans through the list of current states 
#  after every entry to see if there is a possible winning combination.


#predefined valiables.
current_state=[['','',''],['','',''],['','','']]
possitions={'A1':(0,0),'A2':(1,0),'A3':(2,0), 'B1':(0,1),'B2':(1,1),'B3':(2,1), 'C1':(0,2),'C2':(1,2),'C3':(2,2)}

play = True
player = True #start with player one as the firt to play

global player1_points
global player2_points
player1_points=0
player2_points=0




def print_status():
    print("    A    B    C")
    print(f"1.{current_state[0]}")
    print(f"2.{current_state[1]}")
    print(f"3.{current_state[2]}")

    print("****************************************************************")
    print(f'player1: {player1_points}')
    print(f'player2: {player2_points}')


def reset_positions():
    for i in range(3):
        for j in range(3):
            current_state[i][j]=''
    play(player)


def check_win(player):
    if current_state[0][0] == current_state[0][1] == current_state[0][2] != "" or current_state[1][0] ==current_state[1][1] == current_state[1][2] != "" or current_state[2][0] ==current_state[2][1] == current_state[2][2] != "" :
        print(f'player {player} won!!!')
        if player=='1':
            player1_points +=1
        elif player=='2':
            player2_points +=1
        print('****GAME OVER****')
        reset_positions()


    elif current_state[0][0] == current_state[1][0] == current_state[2][0] != "" or current_state[0][1] == current_state[1][1] == current_state[2][1] != "" or current_state[0][2] == current_state[1][2] == current_state[2][2] != "":
        print(f'player {player} won!!!')
        if player=='1':
            player1_points +=1
        elif player=='2':
            player2_points +=1
        print('****GAME ENDED****')
        reset_positions()


    elif current_state[0][0] == current_state[1][1] == current_state[2][2] != "" or current_state[0][2] == current_state[1][1] == current_state[2][0] != "" :
        print(f'player {player} won!!!')
        if player=='1':
            player1_points +=1
        elif player=='2':
            player2_points +=1
        print('****GAME ENDED****')
        reset_positions()


def update_state(possition,entry):
    current_state[possition[0]][possition[1]]= entry
    print_status()


def play( player):
    print("***********STARTING A NEW MATCH***********")
    print_status()
    while play:
        if player == True:
            print("*** player 1 turn....***")
            print("***select possition, ie A1, A2, A3, B1 ...C3.***")
            possition=possitions[input().upper()]
            if current_state[possition[0]][possition[1]] == 'X' or current_state[possition[0]][possition[1]] == 'O':
                print("*** invalid possition***")
                player =True
                
            else:
                entry='X'
                update_state(possition, entry)
                player=False
                check_win(player='1')


        if player == False:
            print("*** player 2 turn....***")
            print("***select possition, ie A1, A2, A3, B1 ...C3.***")
            possition=possitions[input().upper()]
            if current_state[possition[0]][possition[1]] == 'X' or current_state[possition[0]][possition[1]] == 'O':
                print("*** invalid possition***")
                player =False
            else:
                print("***now enter 'X' or an 'O' ***")
                entry='O'
                update_state(possition, entry)
                player=True
                check_win( player='2')


if __name__ =="__main__":
    play(player)

