# Вычислить число pi с заданной точностью d

import math
d = input('Введите требуемую точность: ')
digits = len(d.split('.')[1])
print(round(math.pi, digits))


