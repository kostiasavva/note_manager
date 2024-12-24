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
print('Дата создания заметки: ' + str(created_date.day) + '-' + str(created_date.month) + '-' + str(created_date.year))
issue_date = datetime.date(2024, 12, 29)
print('Дата истечения заметки: ' + str(issue_date.day) + '-' + str(issue_date.month) + '-' + str(issue_date.year))
