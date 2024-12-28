heading = ['Имя пользователя: ', 'Заголовок заметки: ', 'Описание заметки: ', 'некий СПИСОК', 'Дата создания: ', 'Завершить до: ', 'Статус: ']
content = ['некая Строка', 'некая Строка', 'некая Строка', 'некиий СПИСОК', 'некаяя ДАТА', 'некая ДАТА', 'ДА/НЕТ']

content[0] = input('Введите Ваше имя: ')
content[1] = input('Введите заголовок заметки: ')
content[2] = input('Опишите суть заметки: ')

import datetime

# Ввод даты оформления заметки
while True:
    while True:
        created_date_str_day = input('Введите сегодняшшее число: ')
        try: created_date_day = int(created_date_str_day)
        except ValueError:
            print('Введите корректное число!')
            continue
        else:
            if created_date_day > 31 or created_date_day < 1:
                print('Введите корректное число!')
                continue
        break
    while True:
        created_date_str_month = input('Введите текущий месяц цифрами: ')
        try: created_date_month = int(created_date_str_month)
        except ValueError:
            print('Введите корректный номер месяца!')
            continue
        else:
            if created_date_month > 12 or created_date_month < 1:
                print('Введите корректный номер месяца!')
                continue
        break
    while True:
        created_date_str_year = input('Введите текущий год: ')
        try: created_date_year = int(created_date_str_year)
        except ValueError:
            print('Введите год корректно!')
            continue
        else:
            if created_date_year > 2050 or created_date_year < 2024:
                print('Введите год корректно!')
                continue
        break
    try: # Это делается для выяления возможной ошибки ввода не существующего 31 числа (29, 30)
        created_date = datetime.date(created_date_year, created_date_month, created_date_day)
    except ValueError:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nВведите заново КОРРЕКТНУЮ дату!\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        continue
    else: break
content[4] = created_date

# Ввод даты окончания срока выполнения
while True:
    while True:
        issue_date_str_day = input('Введите число даты истечения срока выполнения: ')
        try: issue_date_day = int(issue_date_str_day)
        except ValueError:
            print('Введите корректное число!')
            continue
        else:
            if issue_date_day > 31 or issue_date_day < 1:
                print('Введите корректное число!')
                continue
        break
    while True:
        issue_date_str_month = input('Введите месяц истечения срока цифрами: ')
        try: issue_date_month = int(issue_date_str_month)
        except ValueError:
            print('Введите корректный номер месяца!')
            continue
        else:
            if issue_date_month > 12 or issue_date_month < 1:
                print('Введите корректный номер месяца!')
                continue
        break
    while True:
        issue_date_str_year = input('Введите год истечения срока: ')
        try: issue_date_year = int(issue_date_str_year)
        except ValueError:
            print('Введите год корректно!')
            continue
        else:
            if issue_date_year > 2050 or issue_date_year < 2024:
                print('Введите год корректно!')
                continue
        break
    try: # Это делается для выяления возможной ошибки ввода не существующего 31 числа (29, 30)
        issue_date = datetime.date(issue_date_year, issue_date_month, issue_date_day)
    except ValueError:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nВведите заново КОРРЕКТНУЮ дату!\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        continue
    else: break
content[5] = issue_date

n = input('Введите нужное количество дополнителых полей: ')
while True:
    try: n = int(n)
    except ValueError:
        print('Введите целое число!')
        continue
    else: break

heading[3] = [] # Список дополнительных заголовков
content[3] = [] # Список содержания дополнительных полей
for i in range(n):
    heading[3].append(input(f'Введите заголовок дополнительного поля №{i + 1}: '))
    content[3].append(input('Введите значение: '))

print('========================================================')
print(heading[0] + content[0].capitalize())
print(heading[1] + content[1].capitalize())
print(heading[2] + content[2].capitalize())

for i in range(n):
    print('  ' + str(i + 1) +  '. ' + heading[3][i].capitalize() + ': ' + content[3][i].capitalize())

print(heading[4] + str(created_date.day) + '-' + str(created_date.month))
print(heading[5] + str(issue_date.day) + '-' + str(issue_date.month))

# Проверка "Срок истёк?"
status = False
if datetime.date.today() > issue_date:
    status = True
if status == False:
    content[6] = 'Заметка в работе'
else: content[6] = 'Срок выолнения истёк'
print(heading[6] + content[6])