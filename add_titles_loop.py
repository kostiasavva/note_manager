heading = ['Имя пользователя: ', 'Заголовок заметки: ', 'Описание заметки: ', 'некий СПИСОК', 'Дата создания (ДД-ММ): ', 'Завершить до (ДД-ММ): ', 'Статус: ']
content = ['некая Строка', 'некая Строка', 'некая Строка', 'некиий СПИСОК', 'некаяя ДАТА', 'некая ДАТА', 'ДА/НЕТ']

content[0] = input('Введите Ваше имя: ')
content[1] = input('Введите заголовок заметки: ')
content[2] = input('Опишите суть заметки: ')

from datetime import datetime

# Ввод даты оформления заметки
while True:
    created_date_str = input('Введите сегодняшшее число в формате ДД.ММ.ГГГГ, где ММ - цифрами: ')
    try: created_date = datetime.strptime(created_date_str, '%d.%m.%Y')
    except ValueError:
        print('Введите корректную дату!')
        continue
    break
content[4] = created_date

# Ввод даты окончания срока выполнения
while True:
    issue_date_str = input('Введите дату истечения срока выполнения в формате ДД.ММ.ГГГГ: ')
    try: issue_date = datetime.strptime(issue_date_str, '%d.%m.%Y')
    except ValueError:
        print('Введите корректное число!')
        continue
    break
content[5] = issue_date

heading[3] = [] # Список дополнительных заголовков
content[3] = [] # Список содержания дополнительных полей
i = 0
while True:
    heading[3].append(input(f'Введите заголовок дополнительного поля №{i+1} (или оставьте пустым для завершения): '))
    content[3].append('')
    if heading[3][i] == '':
        heading[3].pop()
        n = i
        break
    else:
        i = i + 1
        continue

for i in range(n):
    content[3][i] = input(heading[3][i].capitalize()+': ')

print('========================================================')
print(heading[0] + content[0].capitalize())
print(heading[1] + content[1].capitalize())
print(heading[2] + content[2].capitalize())

for i in range(n):
    print('  ' + str(i + 1) +  '. ' + heading[3][i].capitalize() + ': ' + content[3][i].capitalize())

print(heading[4] + content[4].strftime('%d-%m'))
print(heading[5] + content[5].strftime('%d-%m'))

# Проверка "Срок истёк?"
status = False

if datetime.today() > issue_date:
    status = True
if not status:
    content[6] = 'Заметка в работе'
else: content[6] = 'Срок выолнения истёк'
print(heading[6] + content[6])