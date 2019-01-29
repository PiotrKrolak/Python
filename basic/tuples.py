"""Do list mozna dodawac, usuwac dane, do tupli nie - nie mozna zmieniac"""


import sys # zeby uzyc metody sys.getsizeof() do porownania rozmiaru tupli i listy w bajtach

list_eg = [1, 2, 3, 'a', 'b', 'c', True, 3.14]
tuple_eg = (1, 2, 3, 'a', 'b', 'c', True, 3.14)

# print(dir(tuple_eg))
print('List size = ', sys.getsizeof(list_eg))
print('Tuple size = ', sys.getsizeof(tuple_eg))
