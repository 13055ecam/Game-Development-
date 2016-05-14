from math import sqrt

#Localisation of the king on the board 
def king_localisation(state):
    for i in range(10):
        for j in range(10):
            if state['people'][i][j] == 'king':
                return (i, j)

# Find a knight nearby the king
def nearby(state, kingcoord):
    close = (20, 20)
    for i in range(10):
        for j in range(10):
            if state['people'][i][j] == 'knight':
                if sqrt(i**2 + j**2) < sqrt(close[0]**2 + close[1]**2):
                    close = (i, j)
    return close

# Sending knights as pathfinders to open a way
def pathfinder(state, kingpos):
    for i in range(10):
        for j in range(10):
            if state['people'][i][j] == 'knight':
                if i == kingcoord[0] - 1 and j == kingcoord[1]:
                    return 'move', i, j, 'N'
    return []

# Pathinder mode
def pathinder_look(state, PEOPLE, knightcoord):
        #create a list of actions
        step = [] 
        for i in range(10):
            for j in range(10):
                if state['people'][i][j] in PEOPLE:
                    if knightcoord[0]-i == 1:
                        step.append(('arrest', knightcoord[0], knightcoord[1], 'S'))
                    elif knightcoord[0]-i == -1:
                        step.append(('arrest', knightcoord[0], knightcoord[1], 'E'))
                    elif knightcoord[1]-i== 1:
                        step.append(('arrest', knightcoord[0], knightcoord[1], 'N'))
                    elif knightcoord[1]-i == -1:
                        step.append(('arrest', knightcoord[0], knightcoord[1], 'W'))
        return step
    
# Action of the king on the board 
def kingmove(kingcoord,card):
    actions = dict()
    sqrt(kingcoord[0]**2 + kingcoord[1]**2)
    kingmovelist = list()
    kingAP = card[0]
    # We give a way for the king to achieve his goal
    while kingcoord[0] != 2 and kingcoord[1] != 2 and kingAP > 0:
        #King moves to the high
        if kingcoord[0] > 2:
            kingmovelist.append(('move', kingcoord[0], kingcoord[1], 'N'))
            kingcoord = (kingcoord[0], kingcoord[1]-1)
            kingAP -= 1
            #King moves on the left
        elif kingcoord[1] > 2:
            kingmovelist.append(('move', kingcoord[0], kingcoord[1], 'W'))
            kingcoord = (kingcoord[0]-1, kingcoord[1])
            kingAP -= 1
    return kingmove

# fonction to move knights on the board based on own position and the king
def knightmove(kingcoord, knightcoord, card, state, PEOPLE):
    #creation a list to put the different position of knights
    knightmovelist = list()
    knightAP = card[1]
    # Knight must be on the board
    while knightAP > 0 and knightcoord[0]<10 and knightcoord[1]<10:
        # Knights respect a accurate location
        if knightcoord == (kingcoord[0]-1, kingcoord[1]):
            # move knight to the the high 
            knightmovelist.append(('move', knightcoord[0], knightcoord[1], 'N'))
            knightcoord = (knightcoord[0]-1, knightcoord[1])
            knightAP -= 1
        # Knights don't respect a accurate location
        if knightcoord != (kingcoord[0]-1, kingcoord[1]):
            while (knightcoord != (kingcoord[0]-1, kingcoord[1]) and knightAP > 0) and (knightcoord != (kingcoord[0]+1, kingcoord[1]) and knightAP > 0):
                for i in range(10):
                    for j in range(10):
                        if state['people'][i][j] in PEOPLE:
            #Knights move based on their coordinates (x,y)
                            if knightcoord[0]-i == 1:
                                knightmovelist.append(('move', knightcoord[0], knightcoord[1], 'E'))
                            elif knightcoord[0]-i == -1:
                                knightmovelist.append(('move', knightcoord[0], knightcoord[1], 'W'))
                            elif knightcoord[1]-i == 1:
                                knightmovelist.append(('move', knightcoord[0], knightcoord[1], 'S'))
                            elif knightcoord[1]-i == -1:
                                knightmovelist.append(('move', knightcoord[0], knightcoord[1], 'N'))
                if knightcoord[0] == 1 and knightcoord[1] == 8:
                    knightmovelist.append(('move', 1, 8, 'N'))
                if knightcoord[1]-kingcoord[1] < -1 and knightcoord[1]+1<10:
                    knightmovelist.append(('move', knightcoord[0], knightcoord[1], 'W'))
                    knightcoord = (knightcoord[0], knightcoord[1]+1)
                    knightAP -= 1

                elif knightcoord[1]-kingcoord[1] > 1 and knightcoord[1]-1>-1:
                    knightmovelist.append(('move', knightcoord[0], knightcoord[1], 'E'))
                    knightcoord = (knightcoord[0], knightcoord[1]-1)
                    knightAP -= 1

                elif knightcoord[0]-kingcoord[0] > 1 and knightcoord[0]-1>-1:
                    knightmovelist.append(('move', knightcoord[0], knightcoord[1], 'S'))
                    knightcoord = (knightcoord[0]-1, knightcoord[1])
                    knightAP -= 1

                elif knightcoord[0]-kingcoord[0] < -1 and knightcoord[0]+1<10:
                    knightmovelist.append(('move', knightcoord[0], knightcoord[1], 'N'))
                    knightcoord = (knightcoord[0]+1, knightcoord[1])
                    knightAP -= 1

    return (knightmovelist, knightAP)






