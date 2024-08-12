def count_calls():                                      # Функция - счётчик
    global calls                                        # Глобальная переменная
    calls = calls + 1
    return

def string_info(string):
    print('Входная строка: ', string)
    count_calls()
    my_kort = len(string), string.upper(), string.lower()
    print(my_kort, ' - Полученный кортеж' )
    return

def is_contains(string, list_to_search):
    count_calls()
    print('Список для поиска: ', list_to_search)
    lst_to_sch_upp = []
    for i in range(len(list_to_search)):
        lst_to_sch_upp.append(list_to_search[i].upper())    # Переводим весь список в верхний регистр
    if string.upper() in lst_to_sch_upp:
        rez = True
    else:
        rez = False
    print(rez)
    print('----------------')
    return rez

calls = 0
string = 'd2d'
list_to_search = ['D2d','F3a','AAAa','Good','a1A']
string_info(string)
is_contains(string, list_to_search)
string = 'd21'
list_to_search = ['22d','A3a','mAAa','Food','C1A']
string_info(string)
is_contains(string, list_to_search)
print('Количество вызовов : ',calls)