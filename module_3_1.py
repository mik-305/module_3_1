def count_calls():
    return

def string_info():
    return

def is_contains(string, list_to_search):
    string = input('Введите строку символов: ')
    if string in list_to_search:
        rez = True
    else:
        rez = False

    #rez = is_contains(string, list_to_search)
    return rez



string = ''
list_to_search = ['Urban', 'URBAN', 'urban', 'Москва']
rez = ''
rez = is_contains(string, list_to_search)
print(rez)