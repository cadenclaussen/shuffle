import shuffle

cards = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]
suits = ["clubs", "dimonds", "spades", "hearts"]
deck = []

for suit in suits:
    for card in cards:
        addCard = card + " " + suit
        addCard = str(addCard)
        deck.append(addCard)    
print(deck)    

print()
print("this is the shuffled deck: ")
print()
newDeck = shuffle.shuffle(deck)
print(newDeck)