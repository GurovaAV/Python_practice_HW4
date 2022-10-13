
input_string = input('Введите элементы списка через пробел: ')
string_splitted = input_string.split(' ')            
my_list = list(map(int,string_splitted))
print(my_list)
new_list = []
for i in my_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)