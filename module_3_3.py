def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = ('Привет', 7, False)
values_dict = {'a': 2, 'b': 'Hello', 'c': 6}
values_list_2 = (True, 7)

print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
print_params() # Параметры остаются те же, что в функции
print_params(3, 2) # Меняется значения первых двух аргументов
print_params(b = 25) # Меняется значение b
print_params(c = [1,2,3]) # Меняется значение c
