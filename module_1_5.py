immutable_var = 4564, 651.5, 'TV', 'tromednoloV'
print(immutable_var)
# так как код после ошибки не будет работать, следующая строка написана комментарием.
# immutable_var[3] = 'tromednoloV'[::-1]
# В Python тип данных "tuple" является не изменяемым.
# Эта строка в коде как бы является ссылкой на сайт с информацией, меняя ссылку пользователь не может повлиять на информацию сайта.
mutable_list = [4564, 651.5, 'TV', 'tromednoloV']
mutable_list[3] = 'tromednoloV'[::-1]
print(mutable_list)