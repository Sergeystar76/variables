my_list = ['apple','banan','pineapple','melon','kiwi','orange']
print('List:',my_list)
print('First element:',my_list[0])
print('Last element:',my_list[-1])
print(my_list[2:5])
print('Sublist:',my_list[2])
my_list[2] = 'limon'
print(my_list)
my_dict = {'apple':'яблоко','banan':'банан','pineapple':'ананас','melon':'дыня','kiwi':'киви','orange':'апельсин'}
print('Dictionary:',my_dict)
key = input('Введите ключ для вывода: ')
print('Translation:',my_dict[key])
key = input('Введите ключ для изменения: ')
key_2 = input('Введите значения для ключа: ')
my_dict.update({key:key_2})
print('Modified dictionary:',my_dict)