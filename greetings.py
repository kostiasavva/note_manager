user_name = 'Петя Васичкин'
print('Имя пользователя: ' + user_name)
title = 'Автомобиль ЗАЗ-968А'
print('Заголовок заметки: ' + title)
content = 'Поменять шаровую опору'
print('Описание заметки: ' + content)
status = False
print('Статус заметки: ' + str(status))
import datetime
created_date = datetime.date(2024, 12, 23)
print('Дата создания заметки: ' + created_date.strftime('%d-%m-%Y'))
issue_date = datetime.date(2024, 12, 29)
print('Дата истечения заметки: ' + issue_date.strftime('%d-%m_%Y'))
# '%B %d, %Y'
# datetime.date.strftime
