import random

roll2 = 0
roll3 = 0 
roll4 = 0
roll5 = 0
roll6 = 0 
roll7 = 0
roll8 = 0
roll9 = 0
roll10 = 0
roll11 = 0
roll12 = 0

def roll():
    global roll2, roll3, roll4, roll5, roll6, roll7, roll8, roll9, roll10, roll11, roll12
    diceRoll1 = random.randint(1, 6)
    diceRoll2 = random.randint(1, 6)
    diceRoll = diceRoll1 + diceRoll2
    if diceRoll == 2:
        roll2 = roll2 + 1
    if diceRoll == 3:
        roll3 = roll3 + 1
    if diceRoll == 4:
        roll4 = roll4 + 1
    if diceRoll == 5:
        roll5 = roll5 + 1
    if diceRoll == 6:
        roll6 = roll6 + 1
    if diceRoll == 7:
        roll7 = roll7 + 1
    if diceRoll == 8:
        roll8 = roll8 + 1
    if diceRoll == 9:
        roll9 = roll9 + 1
    if diceRoll == 10:
        roll10 = roll10 + 1
    if diceRoll == 11:
        roll11 = roll11 + 1
    if diceRoll == 12:
        roll12 = roll12 + 1   
for _ in range(50000):
    roll()
print(roll2)
print(roll3)
print()
print(roll3 / roll2)