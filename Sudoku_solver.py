#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 21:43:56 2018

@author: bfalase
"""

import numpy as np
from collections import Counter, OrderedDict
from pprint import pprint
from Utilities import sudoku_utilities
import time

startTime = time.time()
game = np.zeros((9,9))
game = game.astype(int)
#fillspots = [
#    (1,1,3),(1,2,2),(1,6,6),(1,9,4),
#    (2,3,9),(2,9,3),
#    (3,4,8),(3,8,6),
#    (4,1,1),(4,5,7),(4,7,5),
#    (5,4,9),(5,6,3),
#    (6,3,8),(6,5,5),(6,9,2),
#    (7,2,6),(7,6,1),
#    (8,1,2),(8,7,7),
#    (9,1,5),(9,4,4),(9,8,1),(9,9,8)
#]
positions=[
        """100007300
        608000000
        200300000
        001000002
        847000500
        300000090
        000000703
        000103840
        400068005"""
        ]
positions = positions[0].replace('\n','').replace(' ','')
counter=0
for row in range(9):
    for column in range(9):
        game[row,column] = positions[counter]
        counter +=1
print(game)

continueLooping = True
filledGame = game.copy()
valueCounter = 0
while continueLooping:
    tempGame = filledGame.copy()
    counter = 0
    possibleMovesDict = sudoku_utilities.allPossibleMoves(tempGame)
    for coordinate in possibleMovesDict.keys():
        if len(possibleMovesDict[coordinate]) == 1 and tempGame[coordinate] == 0:
            tempGame[coordinate] = possibleMovesDict[coordinate][0]
            counter += 1
            valueCounter += 1
    filledGame = tempGame
    if counter == 0:
        continueLooping = False
print("Was able to fill in {} moves".format(str(valueCounter)))
pprint(game)
pprint(filledGame)
game = filledGame

#loop through each coordinate key
combos = []
counter = 0
possibleMovesDict = sudoku_utilities.allPossibleMoves(game)
for coordinate in possibleMovesDict.keys():
    counter += 1
    if len(possibleMovesDict[coordinate]) == 1:
        if len(combos) == 0:
            combos.append([(coordinate, possibleMovesDict[coordinate][0])])
        else:
            for index, combo in enumerate(combos):
                combos[index].append((coordinate, possibleMovesDict[coordinate][0]))
    else:
        if len(combos) == 0:
            for value in possibleMovesDict[coordinate]:
                combos.append([(coordinate, value)])
        else:
            #each path in combos needs to be printed x times, x being the length of possible moves
            tempList = []
            for combo in sudoku_utilities.comboGenerator(combos):
                comboGameToCheck = sudoku_utilities.fillGametoTest(game, combo)
                if sudoku_utilities.checkGame(comboGameToCheck):
                    for value in possibleMovesDict[coordinate]:
                        tempList.append(combo + [(coordinate, value)])
            combos = list(tempList)
    print("{}/81 squares solved with a total of {} combinations found".format(len(combos[0]), len(combos)))

solutions = []
for index, combo in enumerate(combos):
    #print("Checking {} / {} games".format(index+1, len(combos)))
    comboGameToCheck = sudoku_utilities.fillGametoTest(game, combo)
    if sudoku_utilities.checkGame(comboGameToCheck):
        solutions.append(comboGameToCheck)
print("Game won!! Found {} solution(s) out of a total of {} choices".format(len(solutions), len(combos)))
endTime = time.time()
totalTime = endTime-startTime
print("Time to solve: {} seconds".format(totalTime))
for solution in solutions:
    pprint(solution)