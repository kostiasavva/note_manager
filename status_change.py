status_0 = 2 # Задаётся изначальный статус "В работе"

def into_word(st_0): # Функция перевода цифры в словесное описание
    st_str = ''
    if st_0 == 1:
        st_str = '"Завершено"'
    elif st_0 == 2:
        st_str = '"В работе"'
    elif st_0 == 3:
        st_str = '"Отложено"'
    return st_str

print('Текущий статус заметки: ' + into_word(status_0))
print('Введите новый статус заметки либо оставьте поле пустым для выхода без изменения')

while True: # Цикл, обрабатывающий ошибочный ввод
    print('   1. Завершено\n   2. В работе\n   3. Отложено')
    status_str = input(f'   Статус:')

    if status_str == '1' or status_str.capitalize() == 'Завершено':
        status = 1
        break
    elif status_str == '2' or status_str.capitalize() == 'В работе':
        status = 2
        break
    elif status_str == '3' or status_str.capitalize() == 'Отложено':
        status = 3
        break
    elif status_str == '':
        status = status_0
        break
    else: print('Введите Ваш выбор корректно цифрой или словами!\n                  =========')

if status == status_0: # Обработка факта изменения статуса
    print('Статус заметки оставлен без изменения: ' + into_word(status))
else: print('Статус заметки изменён на: ' + into_word(status))

