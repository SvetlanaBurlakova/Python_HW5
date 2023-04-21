"""Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит 
число А в целую степень B с помощью рекурсии.
*Пример:*
A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 """

a = int(input('Введите число A: '))
b = int(input('Введите число B: '))

def powerRecur(a,b):
    if b==1:
        return a
    else:
        return a*powerRecur(a,b-1)
    
print(powerRecur(a,b))