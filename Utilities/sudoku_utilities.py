#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 21:40:56 2018

@author: bfalase
"""
import numpy as np
from collections import Counter, OrderedDict
from pprint import pprint

def checkIfGameWon(gameArray):
    if 0 in gameArray:
        return False
    else: return True
def checkForDuplicates(array):
    """Utility Function.
    Arguments:
                array: Numpy array
    Returns:
        Boolean. False if there are no duplicate values in the array. True if there are
        """
    flatArray = array.flatten()
    duplicates = [item for item, count in Counter(flatArray).items() if count > 1]
    if 0 in duplicates:
        duplicates.remove(0)
    if len(duplicates) > 0:
        return True
    else: return False 
def flattenRowColumnandCube(position, tempGame):
    """Utility function.
    Arguments:
                position: Tuple pair of integers
    Returns:
                flatRow, flatCol, FlatCube: flat (9,) array
    """
    #Get a row and column array
    gameRow, gameCol = position
    tempGameRow = tempGame[gameRow, :]
    tempGameCol = tempGame[:, gameCol]
    #get the 9 member square location into its own array
    if gameRow >= 0 and gameRow <= 2 and gameCol >= 0 and gameCol <= 2:
        tempGameCube = tempGame[0:3, 0:3]
    elif gameRow >= 0 and gameRow <= 2 and gameCol >= 3 and gameCol <= 5:
        tempGameCube = tempGame[0:3, 3:6]
    elif gameRow >= 0 and gameRow <= 2 and gameCol >= 6 and gameCol <= 9:
        tempGameCube = tempGame[0:3, 6:9]
    elif gameRow >= 3 and gameRow <= 5 and gameCol >= 0 and gameCol <= 2:
        tempGameCube = tempGame[3:6, 0:3]
    elif gameRow >= 3 and gameRow <= 5 and gameCol >= 3 and gameCol <= 5:
        tempGameCube = tempGame[3:6, 3:6]
    elif gameRow >= 3 and gameRow <= 5 and gameCol >= 6 and gameCol <= 9:
        tempGameCube = tempGame[3:6, 6:9]
    elif gameRow >= 6 and gameRow <= 8 and gameCol >= 0 and gameCol <= 2:
        tempGameCube = tempGame[6:9, 0:3]
    elif gameRow >= 6 and gameRow <= 8 and gameCol >= 3 and gameCol <= 5:
        tempGameCube = tempGame[6:9, 3:6]
    elif gameRow >= 6 and gameRow <= 8 and gameCol >= 6 and gameCol <= 9:
        tempGameCube = tempGame[6:9, 6:9]
    return tempGameRow.flatten(), tempGameCol.flatten(), tempGameCube.flatten()
def copyGameandSetNumberForTesting(position, value, tempGame):
    temporaryGame = tempGame.copy()
    gameRow, gameCol = position
    temporaryGame[gameRow, gameCol] = value
    return temporaryGame
def validatenumber(position, value, tempGame):
    """Utility function. 
    Arguments: 
                Position: Tuple pair of integers
                Value: Integer. Tentative value to be played
    Returns:
                validNumber: Boolean. True if value is valid to play in position. False if value is illegal
    """
    tempGameCopytoCheckIfValidNumber = copyGameandSetNumberForTesting(position, value, tempGame)
    flatRow, flatCol, flatCube = flattenRowColumnandCube(position, tempGameCopytoCheckIfValidNumber)
    if not checkForDuplicates(flatRow) and not checkForDuplicates(flatCol) and not checkForDuplicates(flatCube):
        return True
    else: return False
def allPossibleMoves(game):
    possibleMovesDict = OrderedDict()
    #fill possibleMovesDict at position with valid moves
    for rowPosition in range(game.shape[0]):
        for colPosition in range(game.shape[1]):
            if game[rowPosition][colPosition] != 0:
                possibleMovesDict[(rowPosition,colPosition)] = [game[rowPosition][colPosition]]
            else:
                possibleMovesDict[(rowPosition,colPosition)] = []
                for value in range(1,10):
                    if validatenumber((rowPosition, colPosition), value, game):
                        possibleMovesDict[(rowPosition,colPosition)].append(value)
    return possibleMovesDict
def fillGametoTest(game, values):
    tempGame = game.copy()
    for coordinate, value in values:
        if tempGame[coordinate] == 0:
            tempGame[coordinate] = value
    return tempGame
def checkGame(game):
    for rowPosition in range(game.shape[0]):
        for colPosition in range(game.shape[1]):
            if not validatenumber((rowPosition, colPosition), game[rowPosition, colPosition], game):
                return False
    return True
def comboGenerator(combos):
    for combo in combos:
        yield combo