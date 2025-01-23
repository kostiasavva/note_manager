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
print('========================================================')
print('Имя пользователя: ' + user_name)
print('Заголовок заметки: ' + title)
print('Описание заметки: ' + content)
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
