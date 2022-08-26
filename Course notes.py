# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 12:52:47 2022

@author: KJ
"""

age = '20'

print(f'Mam {age} lat.')
print('Mam {} lat.'.format(age))

# %%

lng = 'Python'
vsn = '3.8'

print(f'Uczęsię języka {lng} w wersji {vsn}')

# %%

price = 199.99
print('Towar kosztuje', price)

# %%
cena = 34.99
waga = 10

print(f'Cena: {cena} PLN. Waga: {waga} kg')

# %%
pi = 3.1415926535

print(f'Przybliżenie liczby pi: {round(pi, 2)}')

# %%
print('=' * 40)
print('autor: jannowak@poczta.com')
print('data: 01-01-2021')
print('=' * 40)

# %%
print('summer', 'time', 'holiday', sep = '#')

# %%
pi = 3.14
print(f'Pole koła wynosi: {pi*5**2} cm2')

# %%
invest = 1000
feet = 0.03


for i in range(5):
    invest += invest * feet
    
print(f'Wartosć końcowa inwestycji wynosi: {round(invest, 2)} PLN')
    
    
# %%
a = 3
b = -4
c = 1

delta = (b**2)-(4*a*c)
print(f'Delta wynosi: {delta}')
    

# %%
suma = 0


for i in range(1,11):
    suma += 10+4*i
    
print(f'Suma pierwszych 10 wyrazów ciągu wynosi: {float(suma)}')

# %%
suma = 0

for i in range(1,7):
    suma += 8*2**(i-1)
    
print(f'Suma pierwszych 6 wyrazów ciągu wynosi: {float(suma)}')

# %%
import math

a=1
b=5
c=4

delta = b**2-4*a*c

root = math.sqrt(delta)

x1 = (-b-root)/2*a
x2 = (-b+root)/2*a

print(f'x1 + x2 = {float(x1+x2)}')
print(f'x1x2 = {round(float(x1*x2), 1)}')
    

# %%
x1 = 2
x2 = -4
y1 = 4
y2 = 6

    
width = (abs(x1) + abs(x2))/2
height = (abs(y1) + abs(y2))/2

if x1>x2:
    width = x1 - width
else:
    width = x2 - width




print(f'Środek odcinka AB: ({float(width)}, {float(height)})')

# %%
bokA = 4
bokB = 3
przekatna = math.sqrt(bokA**2+bokB**2)

print(f'Odległosć punktów A i B wynosi: {float(przekatna)}')


# %%
a=1
b=5
c=4

delta = b**2-4*a*c

root = math.sqrt(delta)

x1 = (-b-root)/2*a
x2 = (-b+root)/2*a

print(f'x1 = {float(x1)}')
print(f'x2 = {float(x2)}')

# %%
g = (4*3*4.5*5) ** (1/4)

print(f'Średnia geometryczna podanych liczb: {round(g, 2)}')

# %%
x=1
y=2
sumam = 1

for i in range(5):
    sumam += x/y
    y = y**2

sumam = round(sumam, 0)
    
print(f'Suma ciągu wynosi: {sumam}')

# %%
a, b, c = 9, 11, 10
srAr = (a+b+c)/3
odchStand = (((a-srAr)**2 + (b-srAr)**2 + (c-srAr)**2)/3)**(1/2)
print(f'Odchylenie standardowe zestawu danych wynosi: {round(odchStand, 2)}')

# %%
filename = 'view.jpg'

makaroni = filename.split('.')
print(makaroni[1])    

# filename = 'view.jpg'
# print(filename[5:])

# %%
text = 'PKV-89415-PLN'
print(text[:3]+text[-3:])

# %%
string = '1 0 0 1 0 1'
string = string.replace(' ', '')
decimal = 0
string = list(string)
for index, letter in enumerate(reversed(string)):
    decimal += int(letter) * 2 ** index
    
print(decimal)

# %%
text = 'Kurs Python'
print(text[::-1])
    
# %%
var1 = ''
var2 = ' '
var3 = '\n'
print(type(var1))
print(type(var2))
print(type(var3))

# %%
var1 = None
var2 = False
var3 = 'True'
print(type(var1))
print(type(var2))
print(type(var3))
    
# %%
flag = False
print(isinstance(flag, bool))

# %%
text = 'python jest popularnym językiem programowania.'

print(text.capitalize())

# %%
print(text.count('p'))

# %%
code1 = 'FVNISJND-XX-2020'
code2 = 'FVNISJND-XY-2019'

print(f'code1: {code1.endswith("2020")}')
print(f'code2: {code2.endswith("2020")}')

# %%
path1 = 'youtube.com/watch?v=5EhRztVxums'
path2 = 'google.com/search?q=car'

if path1.find('youtube') >= 0:
    th1 = True
else:
    th1 = False
if path2.find('youtube') >= 0:
    th2 = True
else:
    th2 = False
    
print(f'path1: {th1}')
print(f'path2: {th2}') 

# %%

base = 'https://e-smartdata.teachable.com/p/'
path1 = base + 'sciezka-data-scientist-machine-learning-engineer'
path2 = base + 'sciezka-data-scientist-deep-learning-engineer'
path3 = base + 'sciezka-bi-analyst-data-analyst'

print(f'path1: {path1.find("scientist")}')
print(f'path2: {path2.find("scientist")}')
print(f'path3: {path3.find("scientist")}')

# %%
code1 = 'FVNISJND-20'
code2 = 'FVNISJND20'
print(f'code1: {code1.isalnum()}')
print(f'code2: {code2.isalnum()}')

# %%
text = 'Google Colab'

print(f'{text.lower()}')

# %%
text = '  Google Colab   '

print(text.strip())

# %%
code = 'FVNISJND-XX'
print(code.replace('-', ' '))

# %%
text = '340-23-245-235'
print(text.replace('-', ''))

# %%

text = 'Open,High,Low,Close'

print(text.split(','))

# %%
text = """Python jest językiem ogólnego przeznaczenia.
Python jest popularny."""

print(text.splitlines())

# %%
num = 34
num = str(num)
print(num.zfill(6))

# %%

url = ('https://e-smartdata.teachable.com/p/'
    'sciezka-data-scientist-machine-learning-engineer')

url = url[36:]
print(url.replace('-', ' '))

# %%

przedmioty = {'matematyka', 'polski'}

przedmioty.add('angielski')

print(przedmioty)

# %%

text = 'Programming in python.'
vowels = {'a', 'e', 'i', 'o', 'u'}

text = text.lower()

text = text.replace('.', '')
text = text.replace(' ', '')
print(text)
text = set(text)
text = text.difference(vowels)
print(f'Liczba elementów: {len(text)}')

# %%
A = {2, 3, 6, 8}
B = {4, 10}
AB = A.symmetric_difference(B)
print(AB)

# %%

ad1_id = {'001', '002', '003'}
ad2_id = {'002', '003', '007'}

ad12 = ad1_id.symmetric_difference(ad2_id)
print(f'Wybrane ID: {ad12}')

# %%
is_clicked = {'9001', '9002', '9005'}
is_bought = {'9002', '9004', '9005'}

isClickedBought = is_clicked.intersection(is_bought)
print(f'ID klientów: {isClickedBought}')


# %%

wig20 = ('CDR', 'PKO', 'PEO')
mwig40 = ('PLW', 'AMC', 'BFT')

allWig = wig20 + mwig40
print(allWig)

# %%

wig20 = ('CDR', 'PKO', 'PEO')
mwig40 = ('PLW', 'AMC', 'BFT')
allWig = (wig20,) + (mwig40,)
print(allWig)

# %%

members = (('Kasia', 23), ('Tomek', 19))

adamTuple = ('Adam', 26)

result = (members[0], adamTuple, members[1])
print(result)

# %%

default = ('YES', 'NO', 'NO', 'YES', 'NO')

yesCount = default.count('YES')

print(f'Liczba wystąpień: {yesCount}')

# %%

names = ('Monika', 'Tomek', 'Adam', 'Olaf')
namesSorted = (names[2], names[0], names[3], names[1])
print(namesSorted)

"""
namesSorted = tuple(sorted(names))
"""

# %%

info = (('Monika', 19), ('Tomek', 21), ('Adam', 18), ('Jarek', 30))

asc = tuple(sorted(info, key=lambda item: item[1]))
desc = tuple(sorted(info, key=lambda item: item[1], reverse = True))

print(f'Rosnąco: {asc}')
print(f'Malejąco: {desc}')    

# %% 

stocks = (('Playway', ('PLW', 310)), ('CD Projekt', ('CDR', 300)))

print(stocks[0][1][0])

# %%

cities = ['Warszawa', 'Łódź', 'Kraków']
cities.append('Gdańsk')

print(cities)

# %%
idx = ['001', '002', '001', '003', '001']

print(f'Liczba wystąpień: {idx.count("001")}')

# %%

text = 'Programowanie w języku Python'
newList = []
newSet = set(text.lower().replace('ę', 'e'))
newList.extend(newSet)
newList.remove(' ')
newList.sort()
print(newList[:10])

# %%

filenames = ['view.jpg', 'bear.jpg', 'ball.png']

filenames.insert(0, 'phone.jpg')
filenames.remove('ball.png')
print(filenames)

# %%

day1 = ['3984', '9042', '4829', '2380']
day2 = ['4231', '5234', '1345', '2455']

day1.extend(day2)
print(day1)


# %%

techs = ('python', 'java', 'sql', 'aws')

techsList = list(techs)

techsList.sort()

techsTupleSorted = tuple(techsList)

print(techsTupleSorted)


# %%

hashtags = ['summer', 'time', 'vibes']

hashes ='#' + '#'.join(hashtags)

print(hashes)


# %%

capitals = {'Poland':'Warsaw', 'Germany':'Berlin', 'Austria':'Vienna'}

print(capitals)

# %%
print(capitals.keys())

# %%

print(capitals.values())


# %%

print(capitals.items())

# %%

dict.get(capitals, 'Austria')

# %%

stocks = {
    'PLW': {'Playway': 316},
    'CDR': {'CD Projekt': 293},
    'TEN': {'Ten Square Games': 301}
}

print(dict.get(stocks, 'PLW'))

# %%

print(stocks.get('TEN').get('Ten Square Games'))

# %%

stocks['CDR']['CD Projekt'] = 310
print(stocks['CDR']['CD Projekt'])

# %%

stocks['BBT'] = {'Boombit': 23}

print(stocks['BBT'])

# %%

ticker = [
    'ALR', 'CCC', 'CDR', 'CPS', 'DNP',
    'JSW', 'KGH', 'LPP', 'LTS', 'MBK',
    'OPL', 'PEO', 'PGE', 'PGN', 'PKN',
    'PKO', 'PLY', 'PZU', 'SPL', 'TPE'
]

tickerWithIndexes = []

n = 0
for i in ticker:
    tickerWithIndexes.append((n, ticker[n]))
    n+=1

print(tickerWithIndexes)

# print(list(enumerate(ticker)))

# %%
tickerWithIndexes = {}
n = 0
for i in ticker:
    tickerWithIndexes[n] = ticker[n]
    n+=1

print(tickerWithIndexes)

# print(dict(enumerate(ticker)))

# %%

project_ids = {
    '01': 'open', 
    '03': 'in progress',
    '05': 'in progress',
    '04': 'completed'
}

a = set(project_ids.values())
b = sorted(list(a))
print(b)

# a.sort()
# %%

stats = {'strona': 'e-smartdata.org', 'ruch': 100, 'typ': 'organiczny'}

stats.pop('ruch')
print(stats)

# %%

users = {'001': 'Marek', '002': 'Monika', '003': 'Jakub'}

print(users.get('005', 'nieokreslony'))

# %%

filename = '01012020_sales.xlsx'

if filename.endswith('xlsx'):
    print('TAK')
else:
    print('NIE')
    
# %%

code = 'DSVNDOICSN'

if code.isupper():
    print('TAK')

# %%

number = 1.0

if isinstance(number, int):
    print('TAK')
else:
    print('NIE')

# %%

password = 'cskdnjcasa#!'

if len(password) >= 11:
    print('Hasło poprawne')
else:
    print('Hasło zbyt krótkie')

# %%

password = 'cskdnjcasa#!'

if len(password) >= 11 and password.__contains__('!'):
    print('Hasło poprawne')
else:
    print('Hasło zbyt krótkie')
    
# %%

project_ids = ['02134', '24253']
project_id = '02135'

if project_id in project_ids:
    print(project_ids)
else:
    project_ids.append(project_id)
    print(project_ids)

# %%

project_ids = {
    '01': 'open', 
    '02': 'new',
    '03': 'in progress',
    '04': 'completed'
}

if project_ids['02'] == 'new':
    project_ids['02'] = 'open'
    
print(project_ids)

# %%

item = '001'
items = ['001', '000', '003', '005', '006']

if item in items:
    items.remove(item)
    
print(items)

# %%
by11Dividable = ''
for i in range(1,100):
    if i%11 == 0:
        by11Dividable += str(i) +','

by11Dividable = by11Dividable[:-1]

print(by11Dividable)

# (','.join(result))

# %%
by11Dividable = ''
for i in range(1,100):
    if i%11 == 0 and i%3 != 0:
        by11Dividable += str(i) +','

by11Dividable = by11Dividable[:-1]

print(by11Dividable)

# %%
result = []
items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]
n = 0
for item in items:
    if item % 2 == 0:
        result.append(item)
print(result)

# %%

items = [1, 5, 3, 2, 2, 4, 2, 4]
result = []
for item in items:
    if item not in result:
        result.append(item)
print(result)

# %%

text = 'Python jest bardzo popularnym językiem programowania'
textList = text.split(' ')
n=0
result = []
for word in textList:
    if n < 4:
        word = word.lower()
        result.append(word)
        n+=1
print(result)

# %%

probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
probabilitiesFiltered = []
for prob in probabilities:
    if prob>0.5:
        probabilitiesFiltered.append(prob)
print(probabilitiesFiltered)

# %%

probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
machineLearning = []
for prob in probabilities:
    if prob>=0.5:
        machineLearning.append(1)
    else:
        machineLearning.append(0)
print(machineLearning)

# %%

items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
itemsDict = {}
for item in items:
    if item in itemsDict.keys():
        itemsDict[item] += 1
    else:
        itemsDict[item] = 1
print(itemsDict)

# %%

text = """Python – język programowania wysokiego poziomu
ogólnego przeznaczenia, o rozbudowanym pakiecie bibliotek
standardowych, którego ideą przewodnią jest czytelność i
klarowność kodu źródłowego."""
text = text.replace('\n', ' ')
textList = text.split(' ')
textFixedList = []
for word in textList:
    word.lower()
    word = word.replace('ą','a')
    word = word.replace('ę','e')
    word = word.replace('ź','z')
    word = word.replace('ż','z')
    word = word.replace('ó','o')
    word = word.replace('ć','c')
    word = word.replace('ś','s')
    word = word.replace(',', '')
    word = word.replace('.', '')
    if len(word) > 10:
        textFixedList.append(word)
        
print(textFixedList)

"""
words = text.split()
words = [word.lower() for word in words]
words = [word.replace('.', '').replace(',', '') for word in words]
words = [word for word in words if len(word) > 10]
print(words)
"""

# %%

indexes = [
    "WIG",
    "WIG-banki",
    "WIG-budownictwo",
    "WIG-CEE",
    "WIG-chemia",
    "WIG-energia",
    "WIG-ESG",
    "WIG-górnictwo",
    "WIG-informatyka",
    "WIG-leki",
    "WIG-media",
    "WIG-motoryzacja",
    "WIG-nieruchomości",
    "WIG-odzież",
    "WIG-paliwa",
    "WIG-Poland",
    "WIG-spożywczy",
    "WIG-telekomunikacja",
    "WIG-Ukraine",
    "WIG.GAMES",
    "WIG.MS-BAS",
    "WIG.MS-FIN",
    "WIG.MS-PET",
    "WIG20",
    "WIG20dvp",
    "WIG20lev",
    "WIG20short",
    "WIG20TR",
    "WIG30",
    "WIG30TR",
    "WIGdiv",
    "WIGtech",
]
# %%
for i in indexes:
    if '20' in i or '30' in i:
        print(i)
        
# %%

gaming = {
    '11B': 362.5,
    'CDR': 297.0,
    'CIG': 0.85,
    'PLW': 318.0,
    'TEN': 300.0
}

for i in gaming:
    if gaming[i] > 100:
        print(i)
        
"""
for ticker, close in gaming.items():
    if close > 100.0:
        print(ticker)
"""

# %%

names = ['Jack', 'Leon', 'Alice', '32-3c', 'Bob']

for name in names:
    if name.isalpha():
        print(f'Hello {name}!')


    














    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
