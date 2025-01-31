import datetime
import time

multi_note = [
    {'name': 'Иван', "title": 'Закупщик', 'descr': 'Ремонт квартиры, руководство, закупка материалов', 'status': 3,
     'c_date': datetime.date(2024, 12, 10), 'i_date': datetime.date(2025, 2, 2)},
    {'name': 'Константин', "title": 'Шофёр', 'descr': 'Съездить привезти стиральную машину', 'status': 1,
     'c_date': datetime.date(2025, 1, 10), 'i_date': datetime.date(2025, 1, 22)},
    {'name': 'Жора', "title": 'Электрик', 'descr': 'Проложить проводку', 'status': 2,
     'c_date': datetime.date(2024, 12, 10), 'i_date': datetime.date(2025, 1, 2)},
    {'name': 'Михаил', "title": 'Сантехник', 'descr': 'Заменить водопроводные трубы', 'status': 2,
     'c_date': datetime.date(2024, 12, 10), 'i_date': datetime.date(2025, 1, 30)},
    {'name': 'Гоша', "title": 'Циклеватель', 'descr': 'Отциклевать паркет', 'status': 1,
     'c_date': datetime.date(2025, 1, 10), 'i_date': datetime.date(2025, 1, 11)},
    {'name': 'Сергей', "title": 'Маляр', 'descr': 'Поклеить обои', 'status': 2,
     'c_date': datetime.date(2024, 12, 30), 'i_date': datetime.date(2025, 1, 20)},
]

def into_word(st_0): # Функция перевода цифры в словесное описание статуса заметки
    st_str = ''
    if st_0 == 1:
        st_str = '"Завершено"'
    elif st_0 == 2:
        st_str = '"В работе"'
    elif st_0 == 3:
        st_str = '"Отложено"'
    return st_str

def note_print(note_): # Функция вывод на экран одной заметки (тип "словарь")
    print(' Имя пользователя: ' + note_['name'])
    print(' Название заметки: ' + note_['title'])
    print(' Описание заметки: ' + note_['descr'])
    print('Статус выполнения: ' + into_word(note_['status']))
    print('    Дата создания: ' + note_['c_date'].strftime('%d.%m.%Y'))
    print('Дата истеч. срока: ' + note_['i_date'].strftime('%d.%m.%Y'))

for i in range (len(multi_note)): # Цикл вывода заметок
    print(f'\n     === Заметка №{i+1} ===')
    note_print(multi_note[i])

print('\nДля поиска нужной записи введите её номер или имя пользователя: ')

while True: # Цикл ввода, одновременно и ошибочного и повторного.
    a_choice = input()
    try: a_choice_int = int(a_choice) # Проверка, введено числом или словами
    except ValueError:
        a_choice_int = len(multi_note) + 1 # Закладывается заведомо ошибочное значение для последующей проверки
        for i in range (len(multi_note)): # Перебор всех имён пользователей
            if a_choice.capitalize() == multi_note[i]['name']:
                a_choice_int = i + 1
                break

    if a_choice_int > len(multi_note) or a_choice_int <= 0:
        print('Такой записи не существует. Введите заново номер/имя пользователя:')
        continue

    print(f'\n     === Заметка №{a_choice_int} ===')
    note_print(multi_note[a_choice_int - 1])
    i_del = input('\nВы уверены, что хотите удалить эту запись? ДА - нажмите "ВВОД", НЕТ -  (любой символ + ВВОД): ')
    if i_del == '':
        deleted = multi_note.pop(a_choice_int - 1)['name']
        print(f'Заметка №{a_choice_int - 1}, "{deleted}" успешно удалена из списка')
        break
    else:
        print('\nВведите номер/имя пользователя другой записи:')
        continue

time.sleep(3) # Задержка вывода оставшихся элементов списка
for i in range (len(multi_note)): # Цикл вывода заметок
    print(f'\n     === Заметка №{i+1} ===')
    note_print(multi_note[i])
