# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 01:02:02 2022

@author: KJ
"""

tab1 = ['-', '-', '-']
tab2 = ['-', '-', '-']
tab3 = ['-', '-', '-']


areaTaken = []


while True:
    print("""|""".join(tab1))
    print("""|""".join(tab2))
    print("""|""".join(tab3))
    print('Pick a place for X.')
    i = 0
    while i<1:
        x = input()
        if x not in areaTaken:            
            areaTaken.append(x)
            i+=1
        else:
            print('Place already taken!')
            x = 0
    x = str(x)
    currentArr = list(x)
    if currentArr[0] == '1':
        tab1[int(currentArr[1])-1] = 'X'
    elif currentArr[0] == '2':
        tab2[int(currentArr[1])-1] = 'X'
    elif currentArr[0] == '3':
        tab3[int(currentArr[1])-1] = 'X'
        
        
    if (tab1[0] == 'X' and tab1[1] == 'X' and tab1[2] == 'X' or
        tab2[0] == 'X' and tab2[1] == 'X' and tab2[2] == 'X' or
        tab3[0] == 'X' and tab3[1] == 'X' and tab3[2] == 'X' or
        tab1[0] == 'X' and tab2[0] == 'X' and tab3[0] == 'X' or
        tab1[1] == 'X' and tab2[1] == 'X' and tab3[1] == 'X' or
        tab1[2] == 'X' and tab2[2] == 'X' and tab3[2] == 'X' or
        tab1[0] == 'X' and tab2[1] == 'X' and tab3[2] == 'X' or
        tab1[2] == 'X' and tab2[1] == 'X' and tab3[0] == 'X'):
        print('Player 1 won!')
        break
        
    print("""|""".join(tab1))
    print("""|""".join(tab2))
    print("""|""".join(tab3))
    print('Pick a place for O.')
    i = 0
    while i<1:
        x = input()
        if x not in areaTaken:            
            areaTaken.append(x)
            i+=1
        else:
            print('Place already taken!')
            x = 0
    x = str(x)
    currentArr = list(x)
    if currentArr[0] == '1':
        tab1[int(currentArr[1])-1] = 'O'
    elif currentArr[0] == '2':
        tab2[int(currentArr[1])-1] = 'O'
    elif currentArr[0] == '3':
        tab3[int(currentArr[1])-1] = 'O'
        
        
    if (tab1[0] == 'O' and tab1[1] == 'O' and tab1[2] == 'O' or
        tab2[0] == 'O' and tab2[1] == 'O' and tab2[2] == 'O' or
        tab3[0] == 'O' and tab3[1] == 'O' and tab3[2] == 'O' or
        tab1[0] == 'O' and tab2[0] == 'O' and tab3[0] == 'O' or
        tab1[1] == 'O' and tab2[1] == 'O' and tab3[1] == 'O' or
        tab1[2] == 'O' and tab2[2] == 'O' and tab3[2] == 'O' or
        tab1[0] == 'O' and tab2[1] == 'O' and tab3[2] == 'O' or
        tab1[2] == 'O' and tab2[1] == 'O' and tab3[0] == 'O'):
        print('Player 2 won!')
        break
    
    
    
    

