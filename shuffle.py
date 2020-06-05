# This is our shuffle program
import random


def shuffle(list):
    newList = []
    listLength = len(list)
    for _ in range(listLength):
        pick = random.choice(list)
        newList.append(pick)
        list.remove(pick)
    return newList
