user_name = input('Введите Ваше имя: ')
title = input('Введите заголовок заметки: ')
content = input('Опишите суть заметки: ')

from datetime import datetime

# Ввод даты оформления заметки
while True:
    created_date_str = input('Введите сегодняшшее число в формате "ДД.ММ.ГГГГ": ')
    try: created_date = datetime.strptime(created_date_str, '%d.%m.%Y')
    except ValueError:
        print('Введите корректное число! День, месяц, год.')
        continue
    else: break
# Ввод даты окончания срока выполнения
while True:
    issue_date_str = input('Введите дату истечения срока выполненияв формате "ДД.ММ.ГГГГ": ')
    try: issue_date = datetime.strptime(issue_date_str, '%d.%m.%Y')
    except ValueError:
        print('Введите корректное число! День, Месяц, Год.')
        continue
    else: break

# К заданию 4:
heading = []
description = []
heading.append(input('Введите заголовок дополнительного поля №1: '))
description.append(input('Введите значение: '))
heading.append(input('Введите заголовок дополнительного поля №2: '))
description.append(input('Введите значение: '))
heading.append(input('Введите заголовок дополнителaьного поля №3: '))
description.append(input('Введите значение: '))

print('========================================================')
print('Имя пользователя: ' + user_name.capitalize())
print('Заголовок заметки: ' + title.capitalize())
print('Описание заметки: ' + content.capitalize())

print(heading[0].capitalize() + ': ' + description[0].capitalize())
print(heading[1].capitalize() + ': ' + description[1].capitalize())
print(heading[2].capitalize() + ': ' + description[2].capitalize())

print('Дата создания: ' + created_date.strftime('%d-%m'))
print('Завершить до: ' + issue_date.strftime('%d-%m'))

# Проверка "Срок истёк?"
status = False
if datetime.today() > issue_date:
    status = True
if status == False:
    status_expired = 'Заметка в работе'
else: status_expired = 'Срок выолнения истёк'
print('Статус заметки: ' + status_expired)
