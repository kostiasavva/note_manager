# Задание 4 add_list {
a = input('Введите заголовок ПЕРВОГО поля: ')
b = input('Введите заголовок ВТОРОГО поля: ')
c = input('Введите заголовок ТРЕТЬЕГО поля: ')
heading = [a, b, c]

a = input(heading[0] + ': ')
b = input(heading[1] + ': ')
c = input(heading[2] + ': ')

content = [a, b, c]

#} Также, блок 2 по данному заданию смотрите ниже

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
    try:
        created_date = datetime.date(created_date_year, created_date_month, created_date_day)
    except ValueError:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nВведите заново КОРРЕКТНУЮ дату!\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        continue
    else: break

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
    try:
        issue_date = datetime.date(issue_date_year, issue_date_month, issue_date_day)
    except ValueError:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nВведите заново КОРРЕКТНУЮ дату!\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        continue
    else: break
print('========================================================')

# Блок 2 по заданию 4 add_list {

print(heading[0] + ' ' + content[0])
print(heading[1] + ' ' + content[1])
print(heading[2] + ' ' + content[2])
#}

print('Дата создания: ' + str(created_date.day) + '-' + str(created_date.month))
print('Завершить до: ' + str(issue_date.day) + '-' + str(issue_date.month))

# Проверка "Срок истёк?"
status = False
if datetime.date.today() > issue_date:
    status = True
if status == False:
    status_expired = 'Заметка в работе'
else: status_expired = 'Срок выолнения истёк'
print('Статус заметки: ' + status_expired)