def send_email(message, recipient, sender='university.help@gmail.com'):
    Domain_Group = ['.com', '.ru', '.net']
# Если "@" нет в recipient или нет any - последовательная проверка на хотябы 1 совподение endswith проверка окончания строки
    if '@' not in recipient or not any(recipient.endswith(domain) for domain in Domain_Group):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    if '@' not in sender or not any(sender.endswith(domain) for domain in Domain_Group):
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
send_email('Вы видите это сообщение как лучший студент Hogwarts!', 'Hogwarts@gmail.com', sender='Hogwarts.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'Hogwarts.student@gmail.com', sender='university.help@gmail.int')
send_email('Напоминаю самому себе о вебинаре', 'Hogwarts.teacher@gmail.com', sender='Hogwarts.teacher@gmail.com')
