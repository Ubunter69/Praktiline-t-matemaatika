#Praktiline töö matemaatika

import random


print("teadmiste kontroll, Matemaatika")
tase1 = ['+', '-']
tase2 = ['*', '/']
tase3 = ['**']

valik = input("Vali ülesannete keerukus:tase1, tase2 või tase3 => ").strip()

if valik not in ["tase1", "tase2", "tase3"]:
    print("VIGA! Vale ülesannete keerukus!")
    exit()


näited = 5
õiged_näited = 0    
for i in range(näited):
    number1=random.randint(1, 100)
    number2=random.randint(1, 50)
    
    if valik=="tase1":
        operation = random.choice(tase1)
    elif valik =="tase2":
        operation = random.choice(tase2)
    elif valik =="tase3":
        operation = random.choice(tase3)
    else:
        print("VALE ülesannete keerukus!")    
    if operation == '+':
        õige_vastus = number1 + number2
        print(f"{number1} + {number2} = ")
    elif operation == '-':
        õige_vastus = number1 - number2
        print(f"{number1} - {number2} = ")
    elif operation == '*':
        õige_vastus = number1 * number2
        print(f"{number1} * {number2} = ")
    elif operation == '/':
        õige_vastus = number1 / number2
        print(f"{number1} / {number2} = ")
    elif operation == '**':  
        number2 = random.randint(1, 3)  
        õige_vastus = number1 ** number2  
        print(f"{number1} ** {number2} = ") 
    else:
        print("Vali õige tase!")
    
    
    try:
        õpilase_vastus = float(input("Teie vastus: "))
        if õpilase_vastus == õige_vastus:
            print("Õige!")
            õige_vastus += 1
        else:
            print(f"Vale. Õige vastus: {õige_vastus}")
    except ValueError:
        print("Palun sisestage number.")

arve = (õiged_näited / näited) * 100

if arve < 60:
    hinne = 2
elif 60 <= arve < 75:
    hinne = 3
elif 75 <= arve < 90:
    hinne = 4
else:
    hinne = 5

print(f"Sa vastasid õigesti {õiged_näited} / {näited} .")
print(f"Sinu hinne: {hinne}")



        
        
