"""
Your module description
"""
'''
print('Hello World!')

print("Python has three numeric types: int, float, and complex")
print("--datos enteros--")
myValue=1
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

print("--datos flotantes--")
myValue=3.14
print(myValue)
print(type(myValue))
print(str(myValue) + " is data type of " + str(type(myValue)))
print("--datos complejos--")
myValue=5j
print(myValue)
print(type(myValue))
print(str(myValue) + " is data type of " + str(type(myValue)))
print("--datos booleanos--")
myValue=False
print(myValue)
print(type(myValue))
print(str(myValue) + " is data type of " + str(type(myValue)))
print('--CADENAS--')
print('Concatenacion')
string1="no "
string2="fap"
strig3= string1 + string2
print(strig3)
print('--INPUTS--')
name = input ('cuál es tu nombre?')
print(name)
color=input('color favorito?')
animal=input('animal favorito?')
print("{}, you like a {} {}!".format(name,color,animal))
'''

'''
print('--TUPLAS, LISTAS, DICCIONARIOS--')
print('--LISTAS--')
fruitList=['manz', 'plat', 'per']
print(fruitList)
print(fruitList[0])
fruitList[1]="sandi"
print(fruitList)
print('--TUPLAS--')
print('las tuplas son INMUTABLES')
myTupla=('ban', 'uva', 'mel')
print(myTupla)
print('--DICCIONARIOS--')
frutaDicc={
    'frutaVerde' : 'aguaca',
    'frutaRoja' : 'fresa',
    'frutaAmarilla' : 'mango'
}
print(frutaDicc)
print(frutaDicc["frutaAmarilla"])
'''

'''
myPacketaxo = [777, 3.1415, False, 'El peluca sabpe', '69']
for item in myPacketaxo:
    print('{} es de tipo {}'.format(item,type(item)))
'''

'''
print('--DATOS COMPUESTOS--')
#Un tipo de datos compuesto es cualquier tipo de datos que comprende 
#tipos de datos primitivos. Si le gusta la comida, puede imaginar un 
#tipo de datos compuesto como si fuera turducken, un plato que consiste en 
#pavo relleno con pato que, a su vez, está relleno con pollo
#Continua en el archivo car_fleet.csv


import csv
import copy

myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

for key, value in myVehicle.items():
    print("{} : {}".format(key,value))
    
myInventoryList = []

with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  
    lineCount = 0  
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
    print(f'Processed {lineCount} lines.')
    
    for myCarProperties in myInventoryList:
        for key, value in myCarProperties.items():
            print("{} : {}".format(key,value))
            print("-----")
'''

'''
#Condicionales
userReply = input("Do you need to ship a package? (Enter yes or no) ")
if userReply == "yes":
    print("We can help you ship that package!")
else:
    print("Please come back when you need to ship a package. Thank you.")
    
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")
'''
    
print('--while--')
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

import random

number = random.randint(1,10)

isGuessRight = False

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
