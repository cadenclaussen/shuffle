import random


def main():
    counter = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    for _ in range(1000000):
        count = roll()
        counter[count] = counter[count] + 1
    for count in range(2, 13):
        print(str(count).rjust(2), ': ', str(counter[count]).rjust(7), " ", int(round(counter[count] / counter[7], 2) * 100), "%")


def roll():
    return random.randint(1, 6) + random.randint(1, 6)


main()
