import random

round=0

player_place=0
cpu_place=0
roll_dice=0


while player_place!=100 and cpu_place!=100:
    round+=1
    old_player_place=player_place
    old_cpu_place=cpu_place
    print(f'player_place={player_place}')
    print(f'cpu_place={cpu_place}')
    roll=input(f"press 'P' to roll the dice {round}: ")
    if roll.lower()=='p':
        print('player turn')
        roll_dice=random.randint(1,6)
        print('dice roll=',roll_dice)
        player_place+=roll_dice
        if player_place==4:
            print('ladder!')
            player_place+=10
            print('4--->14')
        elif player_place==9:
            print('ladder!')
            player_place+=22
            print("9--->31")  
        elif player_place==17:
            print('snake!')
            player_place-=10
            print("17--->7")
        elif player_place==28:
            print('ladder!')
            player_place+=56
            print('28--->84') 
        elif player_place==21:
            print('ladder!')
            player_place+=21
            print('21--->42')
        elif player_place==51:
            print('ladder!')
            player_place+=16
            print('51--->67')
        elif player_place==54:
            print('snake!')
            
            player_place-=20
            print('54--->34')
        elif player_place==62:
            print('snake!')
            
            player_place-=43
            print('62--->19')
        elif player_place==64:
            print("snake!")
            
            player_place-=4
            print('64--->60')
        elif player_place==72:
            print('ladder!')
            player_place+=19
            print('72--->91')
        elif player_place==80:
            print('ladder!')
            player_place+=19
            print('80--->99')
        elif player_place==21:
            print('ladder!')
            player_place+=21
            print('21--->42')
        elif player_place==87:
            print('snake!')
            player_place-=51
            print('87--->36')
        elif player_place==93:
            print('snake!')
            player_place-=20
            print('93--->73')
        elif player_place==98:
            print('snake!')
            player_place-=19
            print('98--->79')
        elif player_place>100:
            print("can't make this move!")
            player_place-=roll_dice
        else:
            print(f"{old_player_place}--->{player_place}")
        if roll_dice==6:
            
            
            while roll_dice==6:
                 print('player bonus!')
                 roll_dice=random.randint(1,6)
                 print('dice roll=',roll_dice)
                 player_place+=roll_dice
                 if player_place==4:
                    print('ladder!')
                    player_place+=10
                    print('4--->14')
                 elif player_place==9:
                    print('ladder!')
                    player_place+=22
                    print("9--->31")  
                 elif player_place==17:
                    print('snake!')
                    player_place-=10
                    print("17--->7")
                 elif player_place==28:
                    print('ladder!')
                    player_place+=56
                    print('28--->84') 
                 elif player_place==21:
                    print('ladder!')
                    player_place+=21
                    print('21--->42')
                 elif player_place==51:
                    print('ladder!')
                    player_place+=16
                    print('51--->67')
                 elif player_place==54:
                    print('snake!')
            
                    player_place-=20
                    print('54--->34')
                 elif player_place==62:
                    print('snake!')
            
                    player_place-=43
                    print('62--->19')
                 elif player_place==64:
                    print("snake!")
            
                    player_place-=4
                    print('64--->60')
                 elif player_place==72:
                    print('ladder!')
                    player_place+=19
                    print('72--->91')
                 elif player_place==80:
                    print('ladder!')
                    player_place+=19
                    print('80--->99')
                 elif player_place==21:
                    print('ladder!')
                    player_place+=21
                    print('21--->42')
                 elif player_place==87:
                    print('snake!')
                    player_place-=51
                    print('87--->36')
                 elif player_place==93:
                    print('snake!')
                    player_place-=20
                    print('93--->73')
                 elif player_place==98:
                    print('snake!')
                    player_place-=19
                    print('98--->79')
                 elif player_place>100:
                    print("can't make this move!")
                    player_place-=roll_dice
                 else:
                    print(f"{old_player_place}--->{player_place}") 
                       
        print('cpu turn') 
        roll_dice=random.randint(1,6)
        print('dice roll=',roll_dice)
        cpu_place+=roll_dice
        if cpu_place==4:
            print('ladder!')
            cpu_place+=10
            print('4--->14')
        elif cpu_place==9:
            print('ladder!')
            cpu_place+=22
            print("9--->31")  
        elif cpu_place==17:
            print('snake!')
            cpu_place-=10
            print("17--->7")
        elif cpu_place==28:
            print('ladder!')
            cpu_place+=56
            print('28--->84') 
        elif cpu_place==21:
            print('ladder!')
            cpu_place+=21
            print('21--->42')
        elif cpu_place==51:
            print('ladder!')
            cpu_place+=16
            print('51--->67')
        elif cpu_place==54:
            print('snake!')
            
            cpu_place-=20
            print('54--->34')
        elif cpu_place==62:
            print('snake!')
            
            cpu_place-=43
            print('62--->19')
        elif cpu_place==64:
            print("snake!")
            
            cpu_place-=4
            print('64--->60')
        elif cpu_place==72:
            print('ladder!')
            cpu_place+=19
            print('72--->91')
        elif cpu_place==80:
            print('ladder!')
            cpu_place+=19
            print('80--->99')
        elif cpu_place==21:
            print('ladder!')
            cpu_place+=21
            print('21--->42')
        elif cpu_place==87:
            print('snake!')
            cpu_place-=51
            print('87--->36')
        elif cpu_place==93:
            print('snake!')
            cpu_place-=20
            print('93--->73')
        elif cpu_place==98:
            print('snake!')
            cpu_place-=19
            print('98--->79')
        elif cpu_place>100:
            print("can't make this move!") 
            cpu_place-=roll_dice
        else:
            print(f"{old_cpu_place}--->{cpu_place}")
        if roll_dice==6:
            
            while roll_dice==6:
                 print('cpu bonus!')
                 roll_dice=random.randint(1,6)
                 print('dice roll=',roll_dice)
                 cpu_place+=roll_dice
                 if cpu_place==4:
                    print('ladder!')
                    cpu_place+=10
                    print('4--->14')
                 elif cpu_place==9:
                    print('ladder!')
                    cpu_place+=22
                    print("9--->31")  
                 elif cpu_place==17:
                    print('snake!')
                    cpu_place-=10
                    print("17--->7")
                 elif cpu_place==28:
                    print('ladder!')
                    cpu_place+=56
                    print('28--->84') 
                 elif cpu_place==21:
                    print('ladder!')
                    cpu_place+=21
                    print('21--->42')
                 elif cpu_place==51:
                    print('ladder!')
                    cpu_place+=16
                    print('51--->67')
                 elif cpu_place==54:
                    print('snake!')
            
                    cpu_place-=20
                    print('54--->34')
                 elif cpu_place==62:
                    print('snake!')
            
                    cpu_place-=43
                    print('62--->19')
                 elif cpu_place==64:
                    print("snake!")
            
                    cpu_place-=4
                    print('64--->60')
                 elif cpu_place==72:
                    print('ladder!')
                    cpu_place+=19
                    print('72--->91')
                 elif cpu_place==80:
                    print('ladder!')
                    cpu_place+=19
                    print('80--->99')
                 elif cpu_place==21:
                    print('ladder!')
                    cpu_place+=21
                    print('21--->42')
                 elif cpu_place==87:
                    print('snake!')
                    cpu_place-=51
                    print('87--->36')
                 elif cpu_place==93:
                    print('snake!')
                    cpu_place-=20
                    print('93--->73')
                 elif cpu_place==98:
                    print('snake!')
                    cpu_place-=19
                    print('98--->79')
                 elif cpu_place>100:
                    print("can't make this move!")
                    player_place-=roll_dice
                 else:
                    print(f"{old_cpu_place}--->{cpu_place}")                 

    else:
        print("wrong command!")

                         

print(f'player_place={player_place}')
print(f'cpu_place={cpu_place}')
    


if player_place==100:
    print('you won!')
else:
    print("you lose!")    
