# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 23:20:15 2022

@author: KJ
"""

list1 = [1, 2, 0]
list2 = [4, 5, 6, 1]

i=-1

for element in list1:
    
    if element in list2:
        print(True)
        break
    i+=1
    if i == len(list1):
        print(False)
    
# %%

hashtags = ['holiday', 'sport', 'fit', None, 'fashion']

i=0

for hashtag in hashtags:
    if not isinstance(hashtag, str):
        print(False)
    elif i == len(hashtags):
        print(True)
    i+=1

# %%

number = 13

i = int(round(number/2+1, 0))
j = i -2

for divider in range(1,i):
    if number % (divider + 1) == 0:
        print('Liczba nie jest pierwsza')
        break
    if j == 0:
        print('13 - liczba pierwsza')
    j-=1


# %%

gaming = {
    '11B': [362.5, 'PLN'],
    'CDR': [74.25, 'USD'],
    'CIG': [0.85, 'PLN'],
    'PLW': [79.5, 'USD'],
    'TEN': [300.0, 'PLN']
}


for inst in gaming.values():
    if inst[1] == 'PLN':
        continue
    else:
        inst[0] *= 4
        inst[1] = 'PLN'
print(gaming)

# %%

names = ['Jack', 'Leon', 'Alice', None, 'Bob']

for name in names:
    if name:
        print(name)
    else:
        continue


# %%

prime = []
num = 1
result = ''

while len(prime) < 10:
    flag = False
    num += 1
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
    if flag != True:
        
        prime.append(num)
for item in prime:
    result += str(item) + ','        

print(result[:-1])

# %%

n = 1
pv = 1000
r = 0.04
fv = 1000
i = 0

while fv < 2000:
    fv += fv*r
    i+=1

print(f'Wartosc przyszla: {round(fv, 2)} PLN. Liczba okresów: {i} lat')


# %%

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 7
start = 0
end = len(numbers) - 1
flag = None




# %%
number = int(input())

while number>2:
    number/=2
if number == 2:
    print(True)
else:
    print(False)
    
# %%

numbers = [1,2,3,4,6,7,10]

rangeArray = [*range(1 , numbers[-1]+1)]
missingArray = []

for number in rangeArray:
    if number not in numbers:
        missingArray.append(number)
        
print(missingArray)

# %%

suma = 3000
counter = 0

try:
    result = suma/counter
    print(result)
except ZeroDivisionError:
    print('Dzielenie przez zero.')

# %%

try:
    with open('file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print('Nie znaleziono pliku.')
    
# %%

users = {'001': 'Marek', '002': 'Monika', '003': 'Jakub'}
user_id = '004'

try:
    print(users[user_id])
except KeyError:
    print(f'Klucz {user_id} nie występuje w słowniku. Dodawanie klucza...')
    users[user_id] = None
print(users)

# %%

with open(r'C:\Users\KJ\.spyder-py3\python_course\CWICZENIA\playway.txt') as f:
    
    lines = f.read().splitlines()
    
    meanArr = []
    i=0
    for line in lines:
        i+=1
        if i == 1:
            continue
        meanArr.append(line.split(',')[-2])
    numbers = 0
    for value in meanArr:
        numbers += int(value)

    
    print(f'3-dniowa srednia cena zamknięcia: '
          f'{round(numbers/(len(meanArr)), 2)}')
    

# %%

indexes = []

with open(r'C:\Users\KJ\.spyder-py3\python_course\CWICZENIA\indeksy.txt') as f:
    
    lines = f.read().splitlines()
    
    for line in lines:
        if line.startswith('WIG'):
            indexes.append(line)
    print(indexes)
    
# %%

with open(r'C:\Users\KJ\.spyder-py3\python_course\CWICZENIA\plw_d.csv'
          , 'r') as file:
    content = file.read().splitlines()
    dataArr = []
    closingArr = []
    
    for element in content[1:]:
        x = element.split(',')
        dataArr.append(x[0])
        closingArr.append(float(x[-2]))
        
    dataClosingPrice = {'Data': dataArr, 'Zamkniecie': closingArr}
    print(dataClosingPrice)
    

# %%

with open(r'C:\Users\KJ\.spyder-py3\python_course\CWICZENIA\plw_d.csv'
          , 'r') as file:
    content = file.read().splitlines()
    wolumenArr = []
    
    for element in content[1:]:
        wolumenArr.append(int(element.split(',')[5]))
    print(f'Max Vol: {max(wolumenArr)}')
        
# %%

with open(r'C:\Users\KJ\.spyder-py3\python_course\CWICZENIA\plw_d.csv'
          , 'r') as file:
    content = file.read().splitlines()
    wolumenArr = []
    contentArr = []
    
    for element in content[1:]:
        wolumenArr.append(int(element.split(',')[5]))
    maxi = max(wolumenArr)
    for element in content[1:]:
         if str(maxi) in element:
             print(f'Data: {element.split(",")[0]}')

# %%

with open(r'C:\Users\KJ\.spyder-py3\python_course\CWICZENIA\num.txt'
          , 'w') as file:
    for number in range(2,19,2):
        file.write(str(number)+'\n')
        
# %%

import json

stocks = {'PLW': ['Playway', 350], 'BBT': ['Boombit', 22]}


with open(r'C:\Users\KJ\.spyder-py3\python_course\CWICZENIA\stocks.json'
          , 'w') as file:
    json.dump(stocks, file, indent=4)
    
# %%


headers = ['user_id', 'amount']
users = [['001', '1400'], ['004', '1300'], ['007', '900']]
headersCSV = ''

for header in headers:
    if headersCSV == '':
        headersCSV += header
    else: headersCSV +=',' + header
    
    
with open(r'C:\Users\KJ\.spyder-py3\python_course\CWICZENIA\users.csv'
          , 'w') as file:
    
    file.write(headersCSV + '\n')
    
    
    for user in users:
        file.write(','.join(user) + '\n')
        
# %%

x = -1.5
expression = 'x**2 + x'

print(eval(expression))

# %%

var1 = 'Python'
var2 = ('Python')
var3 = ('Python',)
var4 = ['Python']
var5 = {'Python'}

print(isinstance(var1, tuple))
print(isinstance(var2, tuple))
print(isinstance(var3, tuple))
print(isinstance(var4, tuple))
print(isinstance(var5, tuple))

# %%

characters = ['k', 'b', 'c', 'j', 'z', 'w']

last = max(characters)
first = min(characters)

print(f'Pierwsza: {last}')
print(f'Ostatnia: {first}')

# %%

ticker = ('TEN', 'PLW', 'CDR')
full_name = ('Ten Square Games', 'Playway', 'CD Projekt')

print(list(zip(ticker, full_name)))
    

# %%

items = (' ', '0', 0.1, True)

print(all(items))

# %%
items = ('', 0.0, 0, False)

print(any(items))

# %%

number = 234

a = str(format(number, 'b')).replace('0', '')
print(len(a))


# %%


def maximum(x, y, z):
    if x>y:
        if x>z:
            return x
        else:
            return z
    elif y>z:
        return y
    else:
        return z

print(maximum(10,12,14))

# %%

def multi(x):
    summary = 1
    for argument in x:
        summary *= argument
    return summary

multi([2,5,7,9])

# %%

def map_longest(wordArr):
    x=0
    y=''
    for word in wordArr:
        
        if len(word)>x:
            x=len(word)
            y = word
    return y

map_longest(['slowo','pisane','lepsze','niz','zagrane'])

# %%

def filter_ge_6(y):
    words = []
    for word in y:
        
        if len(word)>=6:
            words.append(word)
    return words

filter_ge_6(['slowo','pisane','lepsze','niz','zagrane'])


# %%

def factorial(x):
    y = 1
    for number in range(1,x+1):
        y *= number
    return y

factorial(6)

# %%

def count_str(x):
    y = 0
    for element in x:
        if isinstance(element, str):
            y += 1
    return y


count_str(['p', 2, 4.3, None])
        
# %%

def count_str(x):
    y = 0
    for element in x:
        if isinstance(element, str) and len(element)>2:
            y += 1
    return y


count_str([1, '#hello', '', 'python', 'go'])


# %%

def remove_duplicates(x):
    duplicatesRemoved = []
    
    for argument in x:
        if argument not in duplicatesRemoved:
            duplicatesRemoved.append(argument)
    return duplicatesRemoved
            
remove_duplicates([1,2,2,2,2,3,3,3,5,6,7,3,2])


# %%

def is_distinct(x):
    duplicatesCheck = []
    for number in x:
        if number not in duplicatesCheck:
            duplicatesCheck.append(number)
        else:
            return False
            break
    return True

is_distinct([1, 2, 3])

is_distinct([1, 2, 3, 3])
    
    
# %%

def function(idx, l=[]):
    for i in range(idx):
        l.append(i ** 3)
    print(l)

function(3)
function(5, ['a', 'b', 'c'])
function(6)

# %%

def function(*args, **kwargs):
    print(args, kwargs)
    
function(3, 4)
function(x=3, y=4)
function(1, 2, x=3, y=4)

# %%

def is_palindrome(x):
    if x[::-1] == x:
        return True
    else:
        return False
    
# %%

stocks = ['playway', 'boombit', 'cd projekt']

length = list(map(lambda x: len(x) , stocks))
print(length)


# %%

def top_n(arr, n):
    arr.sort(reverse = True)
    newArr = []
    i=0
    while i<n:
        newArr.append(arr[i])
        i+=1
    return newArr

top_n([4, 5, 2, 9, 5, 2, 8, 2, 8, 10], 3)


# %%

def count_none(x):
    i=0
    for arg in x:
        if arg == None:
            i+=1
    return i

count_none([1, None, None, 5, None, 2])

# %%

def dot_product(arr1, arr2):
    i = 0
    n = 0
    while i<len(arr1):
        n += arr1[i]*arr2[i]
        i += 1
    return n

dot_product([7, 3], [7, 20])

# %%

def file_gen(x):
    for arg in x:
        if arg.endswith('.txt'):
            yield arg
            
fnames = ['data1.txt', 'data2.txt', 'data3.txt', 'view.jpg']
list(file_gen(fnames))


# %%

def enum(obj):
    i = 0
    for arg in obj:
        yield  (i, arg)
        i += 1
    
# %%

def dayname(x):
    days = ['pon', 'wt', 'śr', 'czw', 'pt', 'sb', 'nd']
    
    yield days[x-1]
    yield days[x]
    yield days[x+1]
    
    
# %%

omega = {(i, j) for i in range(1, 7) for j in range(1, 7)}
probability = {combo for combo in omega if combo[0] + combo[1] > 10}

print(f'P-stwo: {len(probability) / len(omega):.2f}')


# %%

desc = "Playway: Playway to producent gier komputerowych."

desc = desc.lower().replace(':', '').replace('.', '').split(' ')

uniqueDesc = {word for word in desc}
print(uniqueDesc)

# %%

omega = {(i, j) for i in range(1, 7) for j in range(1, 7)}
probability = {pair for pair in omega if pair[0]**2 + pair[1]**2>=45}
print(f'P-stwo: {round(len(probability)/len(omega), 2)}')


# %%

omega = {(i, j, k) for i in range(1,7) for j in range(1,7)
         for k in range(1, 7)}

probability = {(i, j, k) for i, j, k in omega if (i+j+k)%7==0}

print(f'P-stwo: {round(len(probability)/len(omega), 2)}')

# %%

omega = {(i, j, k) for i in range(1,7) for j in range(1,7)
         for k in range(1, 7)}

probability = {(i, j, k) for i, j, k in omega if (i**2+j**2+k**2)%3==0}

print(f'P-stwo: {round(len(probability)/len(omega), 4)}')


# %%

omega = {(i, j, k) for i in range(1,7) for j in range(1,7)
         for k in range(1, 7)}

probability = {(i, j, k) for i, j, k in omega if 
               i%2==1 and j%2==1 and k%2==1}

print(f'P-stwo: {round(len(probability)/len(omega), 3)}')