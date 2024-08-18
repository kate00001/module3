calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(name):
    result = (len(name), str(name.upper()), str(name.lower()))
    count_calls()
    return (result)


def is_contains(string, list_to_search):
    string = str(string).lower()
    list_to_search = list(list_to_search)
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue
    count_calls()
    return result



print(string_info('Капуста'))
print(string_info('Комбинезон'))
print(is_contains('Крем', ['Для лица', 'кРем для рук', 'КРЕМЕНь']))
print(is_contains('КРУг', ['Михаил Круг', 'КРУГ', 'КВАдрат', 'Крем']))
print(calls)
