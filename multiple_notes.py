print(' Заметки на лету: всё под рукой и вовремя!')

from datetime import datetime, date

multi_note = []
def note_input(mlt_nt):
    def date_input():  # Позволяет ввести дату в любом формате.
        while True:
            created_date_str = input(
                'в формате ДД.ММ.ГГГГ или ГГГГ.ММ.ДД, где ММ - месяц цифрами,\nразделители: точка(.), дробь(/), дефис(-): ')
            try:
                a_date = datetime.strptime(created_date_str, '%d.%m.%Y')
            except ValueError:
                try:
                    a_date = datetime.strptime(created_date_str, '%Y.%m.%d')
                except ValueError:
                    try:
                        a_date = datetime.strptime(created_date_str, '%d/%m/%Y')
                    except ValueError:
                        try:
                            a_date = datetime.strptime(created_date_str, '%Y/%m/%d')
                        except ValueError:
                            try:
                                a_date = datetime.strptime(created_date_str, '%d-%m-%Y')
                            except ValueError:
                                try:
                                    a_date = datetime.strptime(created_date_str, '%Y-%m-%d')
                                except ValueError:
                                    print('Введите КОРРЕКТНУЮ дату\n')
                                    continue
                                break
                            break
                        break
                    break
                break
            break
        a_date = a_date.date()  # Преобразуем timedate в date для возможности сравнения
        return a_date

    l = len(mlt_nt)
    note = {'name': '', 'title': '', 'descr': '', "status": '', 'c_date': '', 'i_date': ''}
    print('Заметка №' + str(l+1))
    note['name'] = input('Введите ваше имя: ').capitalize()
    note['title'] = input('Введите название заметки: ').capitalize() # Озаглавливание для удобства последующего сравнения
    if l == 0: # Обработка первичного ввода для предотвращения зацикливания при сравнении с несуществующим элементом списка
        no_rep = True
    else:
        no_rep = False
    while True: # Цикл повторного ввода названия при повторяющемся значении
        for i in range(1,l+1): # Цикл перебора ранее введённых названий предыдыдущих заметок
            if note['title'] == mlt_nt[i-1]['title']:
                title_ = input('Данное название уже присутствует.\nПодтвердите ввод либо введите новое:')
                if title_ == '':
                    no_rep = True
                    break
                else:
                    note['title'] = title_.capitalize()
                    break # Повторная проверка вновь введёного названия на совпадение (в "while")
            if i == l: # Конец перебора, повторений не выявлено, прерывание "while"
                no_rep = True
        if no_rep:
            break

    note['descr'] = input('Введите описание: ')
    print('Введите статус заметки цифрой или буквами')

    while True:  # Цикл, обрабатывающий ошибочный ввод
        print('   1. Завершено\n   2. В работе\n   3. Отложено')
        status_str = input('   Статус:')

        if status_str == '1' or status_str.capitalize() == 'Завершено':
            status = 1
            break
        elif status_str == '2' or status_str.capitalize() == 'В работе':
            status = 2
            break
        elif status_str == '3' or status_str.capitalize() == 'Отложено':
            status = 3
            break
        else:
            print('Введите Ваш выбор корректно цифрой или словами!\n                  =========')

    note['status'] = status
    print('Введите дату создания заметки')
    note['c_date'] = date_input()
    print('Введите дату истечения срока выполнения заметки')
    note['i_date'] = date_input()

    mlt_nt.append(note)
    return(mlt_nt) # Завершение ввода новой заметки, возврат списка с плюс одним элементом

def into_word(st_0): # Функция перевода цифры в словесное описание статуса заметки
    st_str = ''
    if st_0 == 1:
        st_str = '"Завершено"'
    elif st_0 == 2:
        st_str = '"В работе"'
    elif st_0 == 3:
        st_str = '"Отложено"'
    return st_str

while True: # Цикл ввода заметок
    multi_note = note_input(multi_note)
    cont = input('Продолжить? (для продолженя нажмите "ВВОД", для прерывания введите "Н" ("НЕТ"): ')
    if cont.upper() == 'Н' or cont.upper() == 'НЕТ':
        break
for i in range (len(multi_note)): # Цикл вывода заметок
    print(f'\n     === Заметка №{i+1} ===')
    print(' Имя пользователя: ' + multi_note[i]['name']) # Вывод дат без форматирования: "datetime.date(2001, 1, 1)"
    print(' Название заметки: ' + multi_note[i]['title'])
    print(' Описание заметки: ' + multi_note[i]['descr'])
    print('Статус выполнения: ' + into_word(multi_note[i]['status']))
    print('    Дата создания: ' + multi_note[i]['c_date'].strftime('%d.%m.%Y'))
    print('Дата истеч. срока: ' + multi_note[i]['i_date'].strftime('%d.%m.%Y'))