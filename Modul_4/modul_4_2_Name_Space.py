def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()


test_function()

'''
коробка (функция) inner_function() находится как бы в закрытой коробке (функция) test_function()
и пока мы не откроем коробку test_function()
достать то что лежит в коробке inner_function() не получится
по этому будет ошибка.
'''
inner_function()
