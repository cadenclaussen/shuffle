import random


def main():
    counter = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    for _ in range(1000000):
        count = roll()
        counter[count] = counter[count] + 1
    for count in range(2, 13):
        print(str(count).rjust(2), ': ', str(counter[count]).rjust(7), " ", int(round(counter[count] / counter[7], 2) * 100), "%")


def roll():
    global roll2, roll3, roll4, roll5, roll6, roll7, roll8, roll9, roll10, roll11, roll12
    diceRoll1 = random.randint(1, 6)
    diceRoll2 = random.randint(1, 6)
    count = diceRoll1 + diceRoll2
    return count


main()
