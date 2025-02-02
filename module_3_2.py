def send_email(message, recipient, sender='university.help@gmail.com'):
    domains = ['.com', '.net', '.ru']
    if not ("@" in sender and any(sender.endswith(domain) for domain in domains)) or \
       not ("@" in recipient and any(recipient.endswith(domain) for domain in domains)):
        print('Невозможно отправить письмо с адреса {} на адрес {}'.format(sender, recipient))
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса {} на адрес {}'.format(sender, recipient))
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {} на адрес {}'.format(sender, recipient))
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')