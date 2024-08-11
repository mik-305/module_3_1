def count_calls():
    global calls
    calls = calls + 1
    return

def string_info(string):
    print('Содержимое вх. строки: ',string, 'Длина вх. строки: ', len(string))
    string_out = string.upper() +' + '+ string.lower()
    print(string_out)
    count_calls()
    return

def is_contains(string, list_to_search):
    count_calls()
    string = input('Введите строку символов: ')
    if string in list_to_search:
        rez = True
    else:
        rez = False

    #rez = is_contains(string, list_to_search)
    return rez


calls = 0
string = ''
list_to_search = ['Urban', 'URBAN', 'urban', 'Москва']
#rez = ''
#rez = is_contains(string, list_to_search)
#print(rez)
count_calls()
string = input('ВВЕДИТЕ СТРОКУ СИМВОЛОВ: ')
string_info(string)
print('Количество вызовов функции Count_Calls: ',calls)
