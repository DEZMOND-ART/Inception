def send_email(message, recipient, *, sender='university.help@gmail.com'):
    # Если "@" нет в recipient или нет,endswith проверка окончания строки
    if '@' not in recipient or not recipient.endswith(('.com', '.ru', '.net')):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    if '@' not in sender or not sender.endswith(('.com', '.ru', '.net')):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
        return
    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')


# Тест
send_email('Это сообщение для проверки связи', 'Im@mail.ru')
send_email('Вы видите это сообщение как лучший студент Hogwarts!', 'Hogwarts@gmail.com',
           sender='Hogwarts.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'Hogwarts.student@gmail.com', sender='university.help@gmail.int')
send_email('Напоминаю самому себе о вебинаре', 'Hogwarts.teacher@gmail.com', sender='Hogwarts.teacher@gmail.com')
