import random
from turtle import st


print("                    WELCOME TO BATTLE SHIP!")
print("-----------------------------------------------------------------")

oppoHit = 0
playerHit = 0

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

player_ships = {
    1 : [5, False, 'Carrier'],
    2 : [4, False, 'Battleship'],
    3 : [3, False, 'Cruiser'],
    4 : [3, False, 'Submarine'],
    5 : [2, False, 'Destroyer'],
}

player_placement = {
    "Carrier" : [' ',' ',' ',' ',' '],
    "Battleship" : [' ',' ',' ',' '],
    "Cruiser" : [' ',' ',' '],
    "Submarine" : [' ',' ',' '],
    "Destroyer" : [' ',' '],
    }

oppo_ships = {
    1 : [5, False, 'Carrier'],
    2 : [4, False, 'Battleship'],
    3 : [3, False, 'Cruiser'],
    4 : [3, False, 'Submarine'],
    5 : [2, False, 'Destroyer'],
}

oppo_placement = {
    "Carrier" : [' ',' ',' ',' ',' '],
    "Battleship" : [' ',' ',' ',' '],
    "Cruiser" : [' ',' ',' '],
    "Submarine" : [' ',' ',' '],
    "Destroyer" : [' ',' '],
    }

occupied = []
oppo_occupied = []
player_attacked = []
oppo_attacked = []

def get_input():
    while True:
        reply = input("")
        if reply[0].isalpha() == True:
            if reply[1:].isdigit() == True:
                break
        print("INVALID INPUT")
    
    return reply

def converter(coord):
    coord_col = alphabet.index(coord[0].upper()) + 1
    coord_arr = int(coord[1:])
    return coord_col, coord_arr

def validShip(coords, last_coord, i, x):
    #NEED TO MAKE SURE THAT THE SHIPS CONNECT PROPERLY, AND ARE IN A STRAIGHT LINE

    new_letter = abs(coords[0] - last_coord[0])
    new_num = abs(coords[1] - last_coord[1])
    
    if x > 1:
        if player_placement[player_ships[i][2]][0] != '':
            twodown = player_placement[player_ships[i][2]][x - 2]
            onedown = player_placement[player_ships[i][2]][x - 1]

            if twodown[1] == onedown[1] == str(coords[0]):
                for j in player_placement[player_ships[i][2]]:
                    if j == ' ':
                        print("INVALID PLACEMENT #1")
                        return False
                    if (j[4] == str(coords[1] - 1)) or (j[4] == str(coords[1] + 1)):
                        return True
                print("INVALID PLACEMENT #9")
                return False
            if twodown[1:3] == onedown[1:3] == str(coords[0]):
                for j in player_placement[player_ships[i][2]]:
                    if j == ' ':
                        print("INVALID PLACEMENT #1")
                        return False
                    if (j[5] == str(coords[1] - 1)) or (j[5] == str(coords[1] + 1)):
                        return True
                print("INVALID PLACEMENT #11")
                return False 
            elif len(twodown) == 7 and len(onedown) == 7:
                if twodown[4:6] == onedown[4:6] == str(coords[1]):
                    for x in player_placement[player_ships[i][2]]:
                        if x == ' ':
                            print("INVALID PLACEMENT #2")
                            return False
                        if (x[1] == str(coords[0] - 1)) or (x[1] == str(coords[0] + 1)):
                            return True
                    print("INVALID PLACEMENT #8")
                    return False 
                print("INVALID PLACEMENT #10")
                return False
            elif len(twodown) == 6 and len(onedown) == 6:
                if twodown[4] == onedown[4] == str(coords[1]):
                    for x in player_placement[player_ships[i][2]]:
                        if x == ' ':
                            print("INVALID PLACEMENT #3")
                            return False
                        if (x[1] == str(coords[0] - 1)) or (x[1] == str(coords[0] + 1)):
                            return True
                    print("INVALID PLACEMENT #7")
                    return False 
                else:
                    print("INVALID PLACEMENT #6")
                    return False
                
            print("INVALID PLACEMENT #4")
            return False
    elif x == 1:
        if new_letter + new_num == 1:
            return True
    else:       
        return True
    print("INVALID PLACEMENT #5")
    return False

def dispBoard():
    print("                          PLAYER                          ")
    print("     A     B     C     D     E     F     G     H     I     J")
    print("  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+")
    for y in range(1, 11, 1):
        if y >= 10:
            print((y), end=' ')
        else:
            print((y), end='  ')
        for x in range(1, 11, 1):
            if (x, y) in occupied:
                if (x,y) in oppo_attacked:
                    print(" [X]  ", end='')
                else:
                    print("  O   ", end='')
            elif (x,y) in oppo_attacked:
                print(" [O]  ", end='')
            else:
                print("      ", end='')
        print("")       
        print("  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+")

def dispBoardOppo():
    print("     A     B     C     D     E     F     G     H     I     J")
    print("  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+")
    for y in range(1, 11, 1):
        if y >= 10:
            print((y), end=' ')
        else:
            print((y), end='  ')
        for x in range(1, 11, 1):
            if (x, y) in oppo_occupied:
                print("  O   ", end='')
            else:
                print("      ", end='')  
        print("")       
        print("  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+")
    

def dispBoardAttack():
    print("                      ATTACK OPPONENT                          ")
    print("     A     B     C     D     E     F     G     H     I     J")
    print("  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+")
    for y in range(1, 11, 1):
        if y >= 10:
            print((y), end=' ')
        else:
            print((y), end='  ')
        for x in range(1, 11, 1):
            if (x, y) in player_attacked:
                if (x, y) in oppo_occupied:
                    print(" [X]  ", end='')
                else:
                    print(" [O]  ", end='')
            else:
                print("      ", end='')
        print("")       
        print("  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+")

def genOppoShip(ship):
    resetCoords = True
    while resetCoords == True:
        resetCoords = False
        num_location = random.randint(1,5)
        temp_letter_location = random.randint(0,5)
        oppoShipCoords = []
        coordRandom = random.randint(1,2)
        for x in range(len(oppo_placement[ship])):
            if coordRandom == 1:
                letter_location = alphabet[temp_letter_location]
                oppoCords = converter(letter_location + str(num_location))
                oppoShipCoords.append(oppoCords)
                temp_letter_location += 1
            elif coordRandom == 2:
                letter_location = alphabet[temp_letter_location]
                oppoCords = converter(letter_location + str(num_location))
                oppoCords = converter(letter_location + str(num_location))
                oppoShipCoords.append(oppoCords)
                num_location += 1
        for i in oppoShipCoords:
            if i in oppo_occupied:
                resetCoords = True
    
    counter = 0

    for i in oppoShipCoords:
        oppo_placement[ship][counter] = i
        oppo_occupied.append(i)
        counter += 1
    return 0


def computer_turn():

    while True:
        oppo_attack_num = random.randint(1,10)
        oppo_attack_letter = alphabet[random.randint(0, 9)]
        oppoAttackCoords = converter(oppo_attack_letter + str(oppo_attack_num))
        if oppoAttackCoords not in oppo_attacked:
            break
     
    oppo_attacked.append(oppoAttackCoords)
    dispBoard()
    if oppoAttackCoords in occupied:
        print("COMPUTER HIT!")
        global oppoHit 
        oppoHit += 1
    return True

def player_turn():
    while True:
        print("WHERE WOULD YOU LIKE TO FIRE!")
        player_attack_coords = get_input()

        if player_attack_coords[0].isalpha() == True:
            if player_attack_coords[1:].isdigit() == True:
                player_attack_coords = converter(player_attack_coords)
                if player_attack_coords not in player_attacked:
                    break
        
        print("INVALID TARGET")

    player_attacked.append(player_attack_coords)
    dispBoardAttack()
    if player_attack_coords in oppo_occupied:
            print("YOU HIT!")
            global playerHit 
            playerHit += 1
    return True


print("                          PLAYER                          ")
print("     A     B     C     D     E     F     G     H     I     J")
print("  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+")
last_coord = (-1, -1)
for i in range(10):
    print(i + 1)
    print("  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+")
    
    
print("Time to place your ships!")
for i in range(1,6,1):
    new_Ship = True
    for x in range(player_ships[i][0]):
        next = False
        while next == False:
            while True:
                print("Place your " + str(x + 1) + "/" + str(player_ships[i][0]) + " of your " + player_ships[i][2] + "!")
                ship_location = get_input()
                if ship_location[0].upper() in alphabet:
                    if len(ship_location) == 2:
                        if int(ship_location[1]) > 0  or ship_location < 10: 
                            break
                    elif len(ship_location) == 3:
                        if int(ship_location[1:]) == 10:
                            break 
                print("INVALID LOCATION")

            coords = converter(ship_location)
            if str(coords) not in player_placement[player_ships[i][2]]:
                if new_Ship == False:
                    if validShip(coords, last_coord, i, x) == True:
                        new_Ship = False
                        last_coord = coords
                        player_placement[player_ships[i][2]][x] = str(coords)
                        occupied.append(coords)
                        print(ship_location + " has been placed!")
                        print("                          PLAYER                          ")
                        dispBoard()
                        next = True
                else:
                    new_Ship = False
                    last_coord = coords
                    player_placement[player_ships[i][2]][x] = str(coords)
                    occupied.append(coords)
                    print(ship_location + " has been placed!")
                    dispBoard()
                    next = True                  
            else:
                print("ALREADY USED!") 
    print(player_ships[i][2] + " HAS BEEN DEPLOYED!")

print("ALL YOUR SHIPS HAVE BEEN DEPLOYED!")

#FOR TESTING PURPOSES
'''player_placement = {
    "Carrier" : ['(1, 1)', '(1, 2)', '(1, 3)', '(1, 4)', '(1, 5)'],
    "Battleship" : ['(7, 5)', '(8, 5)', '(9, 5)', '(10, 5)'],
    "Cruiser" : ['(10, 8)', '(10, 9)', '(10, 10)'],
    "Submarine" : ['(1, 10)', '(2, 10)', '(3, 10)'],
    "Destroyer" : ['(5, 1)', '(5, 2)'],
    }

occupied = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (7, 5), (8, 5), (9, 5), (10, 5), (10, 8), (10, 9), (10, 10), (1, 10), (2, 10), (3, 10), (5, 1), (5, 2)]'''


for o in range(1,6,1):
    genOppoShip(oppo_ships[o][2])

gameover = False

while gameover == False:
    player_turn()

    if playerHit == 17:
        print("PLAYER WINS!")
        break

    computer_turn()

    if oppoHit == 17:
        print("COMPUTER WINS!")
        break



        

    





                        
        
        
    

