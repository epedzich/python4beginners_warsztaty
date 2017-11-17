# # Zadanie 1
# # Napisz funkcję power, która dla danego n i p zwraca w wyniku n podniesione do potęgi p.
# # Domyślna wartość argumentu p to 2.
# # Niech n i p będą liczbami całkowitymi >= 0.

# def power(n, p=2):
#     if n >= 0 and isinstance(n, int) and p >= 0 and isinstance(p, int):
#         return n ** p
#     else:
#         raise ValueError('Jako argumenty podaj liczby całkowite większe od zera')

#
#
# print(power(2))
# assert power(5) == 25
# assert power(5, 3) == 125
#
# # Zadanie 2
# # Napisz funkcję copy_reversed, która przyjmuje dwie listy, list_a i list_b
# # i która dodaje do listy list_b całą zawartość list_a, ale w odwróconej kolejności.
# # Funkcja copy_reversed niech zwraca None.
#
# x = [1, 2, 3]
# y = [4, 5, 6]
#
# def copy_reversed(list_a, list_b):
#     return list_b.extend(list_a[::-1])
#
# result = copy_reversed(x, y)
# #
# #
# # assert y == [4, 5, 6, 3, 2, 1]
# # assert result is None
#
# # Zadanie 3
# # Napisz funkcję, add_one, która przyjmuje jako argument listę.
# # Do podanej listy powinien zostać dodany nowy element: 1, a następnie lista powinna zostać zwrócona z funkcji.
# # Argument w funkcji niech będzie opcjonalny - w przypadku, gdy funkcja nie otrzyma żadnego argumentu, niech zachowuje się tak, jakby otrzymała pustą listę.
#
# def add_one(lista = None):
#     if lista is None:
#         lista = []
#     lista.append(1)
#     return lista
#
# test_list = [5, 6, 7]
# result1 = add_one(test_list)
# assert result1 == [5, 6, 7, 1]
#
# result2 = add_one()
# assert result2 == [1]
#
# result3 = add_one()
# assert result3 == [1]

# Zadanie 4
# Napisz funkcję factorial, która dla danego n obliczy rekurencyjnie silnię

# def factorial(n):
#     if n < 1:
#         return 1
#     else:
#         result = n * factorial(n - 1)
#         return result
#
# assert factorial(5) == 120

# Zadanie 5
# Napisz funkcję function_results_sum, która przyjmuje dowolną liczbę funkcji
# jako argumenty pozycyjne.
# Argumenty do poszczególnych funkcji przekazywane są do function_results_sum jako keyword arguments w
# postaci NAZWA_FUNKCJI=ARGUMENTY.
# Funkcja function_results_sum powinna zwrócić sumę wyników otrzymanych
# po odpaleniu każdej z funkcji z odpowiednimi argumentami.
# Jeżeli funkcja jest bezargumentowa, nie oczekuje się podania do niej
# argumentów
# Gdy funkcja przyjmuje jeden argument, jako keyword argument przekazany
# będzie int, np. one_arg_function_name=2
# Gdy funkcja przyjmuje więcej argumentów - oczekiwana jest tupla odpowiedniej
# długości, np. two_args_function_name=(1, 2)

# przykład 1:
# sygnatury funkcji:
# def no_arg()
# def one_arg(a)
# def multiple_args(a, b, c, e, f)
#
# wywołanie function_results_sum:
# function_results_sum(
#     no_arg, one_arg, multiple_args,
#     one_arg=23,
#     multiple_args=(1, 2, 3, 4, 5)
# )

# inne wywołanie function_results_sum:
# function_results_sum(
#     no_arg, one_arg, multiple_args,
#     one_arg=-1245
#     multiple_args=(45, 65, 76, 123456, 111.222)
# )
#
# W zadaniu skorzystaj z atrybutu __name__ dostępnego na obiekcie funkcji
# #
# def no_arg():
#     return 5
#
#
# def ident(x):
#     return x
#
#
# def mult(x, y):
#     return x * y
#
# def function_results_sum(*functions, **kwargs):
#     suma = 0
#     for func in functions:
#         name = func.__name__
#         args = kwargs.get(name, [])
#         if isinstance(args, (tuple, list)):
#             suma += func(*args)
#         else:
#             suma += func(args)
#
#     return suma
# #
# assert function_results_sum(no_arg, ident, mult, ident=2, mult=(3, 4)) == 19
# #
#
#
# # Zadanie 6
# # Jesteś administratorem Bardzo Wysokiego Budynku Biurowego BWBB.
# # Masz listę ile osób znajduje się na kolejnych piętrach BWBB: `lista_osob` (czyli wartość lista_osób[5] to liczba osób na piętrze nr 5) - zawiera ona tylko liczby całkowite
# W budynku znajduje się określona liczba ewakuacyjnych klatek schodowych: `liczba_klatek_schodowych` - jest to liczba całkowita
# Każda z klatek pozwala na jednoczesne poruszanie się kilku osób obok siebie: `liczba_osob_w_rzedzie` (liczba całkowita).
# Odstęp czasowy miedzy każdym ewakuowanym rzędem osób to 1 sekunda.
# `tempo_schodzenia` to liczba sekund potrzebna na przejście jednego piętra. Uznajemy, że wszyscy schodzą w tym samym tempie
# Ewakuacja budynku zaczyna się od najwyższego piętra, piętro po piętrze w dół.
# Po jakim czasie powinna zaczynać się ewakuacja dla poszczególnych pięter żeby nie tworzyły się zatory?
# Zatory nie tworzą się wtedy, gdy osoby z wyższych minęły już piętro, które jest w danym momencie ewakuowane.
# Funkcja ewakuacja powinna zwracać listę z intami po ilu sekundach od rozpoczęcia ewakuacji budynku  na każdym piętrze zostanie włączony alarm
# czyli result[6] przechowuje po ilu sekundach został włączony alarm na szóstym piętrze

# Osoby ewakuowane same rozkładają się po równo na liczbę zejść ewakuacyjnych
# Piętro zaczyna się ewakuować od razu po uruchomieniu na nim alarmu
# Argumenty do funkcji będą przekazane po nazwie, jako keyword
# from math import ceil
#
# def ewakuacja(lista_osob, liczba_klatek_schodowych, liczba_osob_w_rzedzie, tempo_schodzenia):
#     result = []
#     rzedy = liczba_klatek_schodowych * liczba_osob_w_rzedzie
#     oproznienie_pietra = 0
#     for i in lista_osob[::-1]:
#         result.append(oproznienie_pietra)
#         oproznienie_pietra += tempo_schodzenia + ceil(i/rzedy)
#
#     return result[::-1]
#
#
# lista_osob = [5, 10, 15]
# liczba_klatek_schodowych = 2
# liczba_osob_w_rzedzie = 1
# tempo_schodzenia = 30
#
# print(ewakuacja(lista_osob, liczba_klatek_schodowych, liczba_osob_w_rzedzie, tempo_schodzenia))
#
# assert [73, 38, 0] == ewakuacja(
#     lista_osob=lista_osob,
#     liczba_klatek_schodowych=liczba_klatek_schodowych,
#     liczba_osob_w_rzedzie=liczba_osob_w_rzedzie,
#     tempo_schodzenia=tempo_schodzenia
# )


class Vector():
    def __init__(self, *args):
        # print(args)
        self.coords = list(args)

    def __repr__(self):
        template = '{}({})'
        name = self.__class__.__name__
        args = ', '.join(repr(x) for x in self.coords)
        # print(name, args)
        return template.format(name, args)

    def __add__(self, other):
        tmp = [x + y for x, y in zip(self, other)]
        return Vector(*tmp)

    def __iadd__(self, other):
        for i in range(len(self)):
            self[i] += other[i]
        return self

    def __radd__(self, other):
        return self + other

    def __len__(self):
        return len(self.coords)

    def __eq__(self, other):
        for i in range(len(self)):
            if not self[i] == other[i]:
                return False
        return True

    def __getitem__(self, item):
        return self.coords[item]

    def __setitem__(self, key, value):
        self.coords[key] = value


looks_like_vector = [0, 1, 2, 3]
v3 = Vector(3, 2, 1, 0)
v4 = v3 + looks_like_vector
v5 = looks_like_vector + v3
assert v4 == v5
assert isinstance(v4, Vector)
assert isinstance(v5, Vector)
assert 'Vector(3, 3, 3, 3)' == str(v4)

v6 = Vector(0, 1, 2, 3)
assert v6 == looks_like_vector
assert looks_like_vector == v6
