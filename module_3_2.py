def send_email(message, recipient, *, sender='university.hel@pgmail.com'):
    endings = ('.com', '.ru', '.net')
    if '@' not in recipient or '@' not in sender:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif recipient.endswith(endings) is False or sender.endswith(endings) is False:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    else:
        if str(recipient) == str(sender):
            print('Невозможно отправить письмо самому себе')
        elif str(sender) != 'university.hel@pgmail.com':
            print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)
        else:
            print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)


send_email('Сообщение', 'kiss_ka00@mail.ru')
