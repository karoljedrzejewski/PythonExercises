# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 02:05:45 2022

@author: KJ
"""

import random

player = 0
comp = 0

def rPSLogic():
    global comp
    global player
    if (user == figures[0] and cptr == figures[1] or
        user == figures[1] and cptr == figures[2] or
        user == figures[2] and cptr == figures[0]):
        print('You lose!')
        comp += 1
        
    elif (user == figures[0] and cptr == figures[2] or
        user == figures[1] and cptr == figures[0] or
        user == figures[2] and cptr == figures[1]):
        print('You win!')
        player += 1
        
    elif user == cptr:
        print('Draw')
        player += 1
        comp += 1
    
    else:
        print('Something went wrong :(')

figures = ['Rock', 'Paper', 'Scissors']

while True:
    print(figures)
    print('Pick 1, 2 or 3')
    x = input()
    try:
        user = figures[int(x)-1]
    except:
        raise ValueError('Thats not 1, 2 or 3!')
    cptr = random.choice(figures)
    print(f'Computer picks {cptr}.')
    print(f'{user} vs {cptr}')
    rPSLogic()
    print(f'{player} : {comp}')
    
    
    
        