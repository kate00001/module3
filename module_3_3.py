def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = ('Привет', 7, False)
values_dict = {'a': 2, 'b': 'Hello', 'c': 6}
values_list_2 = (True, 7)

print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
