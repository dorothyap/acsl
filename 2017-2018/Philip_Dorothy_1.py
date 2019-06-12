# Dorothy Philip Dec 16, 2017
# ACSL 2017 - 2018 ACSL Ninety-Nine

def get_face_value(current_total, card) : # defining 2 variables
    if card == 9 : # goes through the card values checking weather it is equal to 9
        return 0 #if equal to 9 return nothing
    elif card == 4 : # checks weather card value is equal to 4
        return -10 # if equal to 4 subtract 10
    elif card == 0 : # checks weather the card value is equal to 0
        if current_total + 11 > 99 : # if value equal to 0 and if you add eleven it is greater than 99
            return 1 #add 1
        else :#otherwise if the result is less than 99
            return 11 # add 11
    else : 
        return card # if not a special condition return card as it is

def deal(total, mycard, dealer) : #defining 3 variables (both the players cards and the total)
    new_total = total # the total value
    my_turn = True #I go first
    for x in dealer : #number in the set
         if my_turn : #if it is part of your cards
             playcard = mycard[0] 
             new_total = new_total + get_face_value(new_total, playcard) #checking whether the number is a special case
             mycard = mycard[1:]  # your cards after that
             mycard.append(x)#adding one of the dealers cards to you pile
         else : #other player
             new_total = new_total + get_face_value(new_total, x)# checking whether the number is a special case
         if new_total > 99 : #if number greater than 99 stop the code
            break #come out of the loop
         my_turn = not my_turn #when you are not going giving the turn to the other player

    winner = 'player' #if you are the winner
    if my_turn : #if I played dealer is the winner
        winner = 'dealer' #if dealer is the winner
    return (new_total, winner) #output

results = [] #empty sequence
for i in range(5) : #5 inputs
    data = raw_input() #input
    input_values = data.split(', ') #splitting the input
    point_total = int(input_values[0]) #value of point total
    mycards = [int(x) for x in input_values[1:4]] #your cards in the seit
    dealercards = [int(x) for x in input_values[4:]] #Dealer cards in the set
    (total, winner) = deal(point_total, mycards, dealercards) # The output
    s = str(total) + ', ' + winner #makes a string and adds ','
    results.append(s)
    
for i in range(5):
    print results[i] #print the output



'''   
87, 5, 8, 9, 7, 4, 6, 3, 9, 0, 2
78, 2, 4, 8, 3, 8, 5, 0, 6, 9, 8
85, 7, 9, 7, 6, 5, 9, 4, 5, 0, 1
84, 8, 4, 2, 7, 9, 0, 1, 9, 8, 3
95, 9, 0, 9, 0, 1, 0, 1, 0, 2, 5
'''
