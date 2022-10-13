# Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл
# многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from io import StringIO
import sys
import random
  
k = int(input('Введите степень многочлена: '))
count = k
my_list = []
while count > 1:
    buffer = StringIO()
    sys.stdout = buffer
    print(random.randint(0,100),'*','x^',count, end = ' + ', sep = '')
    first = buffer.getvalue()
    sys.stdout = sys.__stdout__
    my_list.append(first)
    count-=1
while count > 0:
    buffer = StringIO()
    sys.stdout = buffer
    print(random.randint(0,100),'*','x', end = ' + ', sep = '')
    second = buffer.getvalue()
    sys.stdout = sys.__stdout__
    my_list.append(second)
    count-=1
while count == 0:
    buffer = StringIO()
    sys.stdout = buffer
    print(random.randint(0,100), end = ' = 0 ', sep = '')
    third = buffer.getvalue()
    sys.stdout = sys.__stdout__
    my_list.append(third)
    count-=1
  
str = ''.join(my_list)
# print('***')
# print(str)

with open ('out.txt', 'w') as f:
    f.write(str)