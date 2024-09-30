my_dict = {'Эдисон': 1847, 'Тесла': 1856, 'Пильчиков': 1857}
print('словарь:', my_dict)
print('существующее значение:', my_dict['Тесла'])
print('не существующее значение:', my_dict.get('Ломоносов'))
my_dict.update({'Влад': 1997, 'Соня': 1998})
deleted_value = my_dict.pop('Эдисон')
print('удаленное значение:', deleted_value)
print('модифицированный словарь:', my_dict)
my_set = {7, 7, 'звук', 'звук', 654.564}
print('множество', my_set)
my_set.update({'щербет', 18})
my_set.remove(654.564)
print('измененное множество', my_set)
