my_dict = {'Anna': 1991, 'Denis': 1992, 'Lena': 1993}
print(my_dict)
print(my_dict['Lena'])
print(my_dict.get('Nina'))
my_dict.update({'Natalya': 1996,
                'Olga': 1997})
a = my_dict.pop('Natalya')
print(a)
print(my_dict)




my_set = {1, 1, 2, 2, 3, 3,'Atom', 4.6}
print(my_set)
a = my_set.add(5)
a = my_set.add('True')
print(my_set)