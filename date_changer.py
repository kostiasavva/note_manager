user_name = 'Петя Васичкин'
print('Имя пользователя: ' + user_name)
title = 'Автомобиль'
print('Заголовок заметки: ' + title)
content = 'Поменять шаровую опору'
print('Описание заметки: ' + content)
status = False
import datetime
created_date = datetime.date(2024, 12, 23)
issue_date = datetime.date(2024, 12, 29)
if datetime.date.today() > issue_date:
    status = True
if status == False:
    status_expired = 'Заметка в работе'
else: status_expired = 'Срок выолнения истёк'
print('Статус заметки: ' + status_expired)
print('Дата создания: ' + str(created_date.day) + '-' + str(created_date.month))
print('Завершить до: ' + str(issue_date.day) + '-' + str(issue_date.month))
