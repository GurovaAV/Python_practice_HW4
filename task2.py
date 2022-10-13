# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input('Введите число: '))
prost_mnog = []
d = 2
while d * d <= num:
    if num % d == 0:
        prost_mnog.append(d)
        num //=d
    else:
        d +=1
if num > 1:
    prost_mnog.append(num)
print(prost_mnog)