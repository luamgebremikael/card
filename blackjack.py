import random
playerIn=True
dealerIn=True




#deck of cards/player dealer hand
deck=[2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10
,'J','Q','K','A','J','Q','K','A','J','Q','K','A','J','Q','K','A']
playerHand = []
dealerHand=[]

#deal the cards
def dealcard(turn):
    card=random.choice(deck)
    turn.append(card)
    deck.remove(card)




#calculate the total of each hand 
def total(turn):
    total = 0
    face = ['A','J','K','Q']
    for card in turn:
        if card in range(1,11):
            total +=card
        elif card in face:
            total += 10
        else:
            if total > 11:
                totsl +=11
    return total





#check for winner 
def revealDealerHand():
    if len(dealerHand)==2:
        return dealerHand[0]
    elif len(dealerHand) >2:
        return dealerHand[0],dealerHand[1]   




#game loop
for _ in range(2):
    dealcard(dealerHand)
    dealcard(dealerHand)

while playerIn or dealerIn:
    print(f"Dealer had {revealDealerHand()} and X")
    print(f"you have {playerHand}for a total of {total(playerHand)}")
    if playerIn:
        stayorHit= input("1:stay\n2:Hit\n")
    if total(dealerHand) > 16:
        dealerIn = False
    else:
        dealcard(dealerHand)    
    if stayorHit=='1':
        playerIn = False    
    else:
        dealcard(playerHand)   
    if total(playerHand)>=21:
        break 
    elif total(dealerHand) >=21:
        break  


if total(playerHand)==21:
    print(f"\nyou have{playerHand}for a total of {total(playerHand)} and the dealer has {dealerHand}for a total of {total(dealerHand)}")   
    print("Blackjack!Winner!")
elif total(dealerHand)==21:
     print(f"\nyou have{playerHand}for a total of {total(playerHand)} and the dealer has {dealerHand}for a total of {total(dealerHand)}")      
     print("Blackjack!Dealer is a Winner!")
elif total(playerHand)>21:
     print(f"\nyou have{playerHand}for a total of {total(playerHand)} and the dealer has {dealerHand}for a total of {total(dealerHand)}")   
     print("Dealer wins!")
elif total(dealerHand)>21:
     print(f"\nyou have{playerHand}for a total of {total(playerHand)} and the dealer has {dealerHand}for a total of {total(dealerHand)}")   
     print("Dealer busts!you win!")
elif 21 - total(dealerHand)>21 - total(playerHand):
     print(f"\nyou have{playerHand}for a total of {total(playerHand)} and the dealer has {dealerHand}for a total of {total(dealerHand)}")   
     print("you win!")