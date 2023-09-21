# Задача 10: 
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.

# 1 - орел
# 0 - решка

n = int(input('Введите количество монет: '))

r = 0 # Количество монет, которые лежат решкой вверх
g = 0 # Количество монет, которые лежат гербом вверх

for x in range(n):    
    coin = int(input('Укажите, какой стороной лежит монета: если вверх решкой - введите 0, если гербом - введите 1: '))
    if coin == 0: # Считаем количество решек и гербов
       r += 1
    else:
       g += 1

if r > g: #Если решек больше, чем гербов, то целесообразно переворачивать гербы и наоборот
     result = n - r
else:
     result = n - g

print('Минимальное количество монет, которое нужно перевернуть:', result)

    

