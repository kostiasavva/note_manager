from datetime import datetime, date

def date_input(): # Позволяет ввести дату в любом формате.
    while True:
        created_date_str = input('в формате ДД.ММ.ГГГГ или ГГГГ.ММ.ДД, где ММ - месяц цифрами,\nразделители: точка(.), дробь(/), дефис(-): ')
        try: a_date = datetime.strptime(created_date_str, '%d.%m.%Y')
        except ValueError:
            try: a_date = datetime.strptime(created_date_str, '%Y.%m.%d')
            except ValueError:
                try: a_date = datetime.strptime(created_date_str, '%d/%m/%Y')
                except ValueError:
                    try: a_date = datetime.strptime(created_date_str, '%Y/%m/%d')
                    except ValueError:
                        try: a_date = datetime.strptime(created_date_str, '%d-%m-%Y')
                        except ValueError:
                            try: a_date = datetime.strptime(created_date_str, '%Y-%m-%d')
                            except ValueError:
                                print('Введите КОРРЕКТНУЮ дату\n')
                                continue
                            break
                        break
                    break
                break
            break
        break
    a_date = a_date.date() # Преобразуем timedate в date для возможности сравнения
    return a_date

# Ввод даты оформления заметки
print('Введите дату оформления заметки')
created_date = date_input()

# Ввод даты окончания срока выполнения
print('Введите дату истечения срока выполнения')
issue_date = date_input()

print('Сегодня ' + datetime.today().strftime('%d.%m.%Y') + ' года.')
print('Дата создания заметки: ' + created_date.strftime('%d.%m.%Y'))
print('Завершить до: ' + issue_date.strftime('%d.%m.%Y'))

# Проверка "Срок истёк?"
if date.today() < issue_date:
    status = 1
if date.today() == issue_date:
    status = 0
if date.today() > issue_date:
    status = -1

if status == 1:
    print('Осталось ' + str((issue_date - date.today()).days) + ' день (дня, дней) до истечения срока выполнения.')
elif status == 0:
    print('Срок выполнения истекает сегодня!')
elif status == -1:
    print('Срок выполнения истёк ' + str((date.today() - issue_date).days) + ' день (дня, дней) назад!')