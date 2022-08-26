# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 22:50:56 2022

@author: KJ
"""

import random
import sys

croupierSum = 0
playerSum = 0

def handDraw(x):
    while x>0:
        global playerSum
        draw = random.choice(cards)
        playerHand.append(draw)
        playerSum += cardsDict[draw]
        x-=1
        
def croupierDraw():
    global croupierSum
    draw = random.choice(cards)
    croupierHand.append(draw)
    croupierSum += cardsDict[draw]
    
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
cardsDict = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10,
             'J':10, 'Q':10, 'K':10, 'A':11}
cardsInGame = []
playerHand = []
croupierHand = []
handDraw(2)


while True:
    print(playerHand)
    if playerSum == 21:
        break
    elif playerSum > 21:
        print('You lost!')
        sys.exit('You lost')
    print('Draw or pass?')
    choice = input()
    if choice == 'draw':
        handDraw(1)
    elif choice == 'pass':
        break
    
while True:
    if playerSum>=croupierSum:
        croupierDraw()
    print('Drawing...')
    print(croupierHand)
    if (croupierSum > 21 or croupierSum>playerSum
    or croupierSum>16 and croupierSum == playerSum):
        break
if croupierSum == 21:
    print('You lost!')
elif croupierSum > 21 or croupierSum < playerSum:
    print('Oh shoot, you won!')
elif croupierSum > playerSum:
    print('You lost!')
elif croupierSum == playerSum:
    print('Thats a draw!')





