# Napisz kod transformujący podany słownik:
# {
#     1: 'Poniedziałek',
#     2: 'Wtorek',
#     3: 'Środa',
#     4: 'Czwartek',
#     5: 'Piątek',
#     6: 'Sobota',
#     7: 'Niedziela'
# }
# do postaci:
# {
#     'Poniedziałek': 1,
#     'Środa': 3,
#     'Piątek': 5,
#     'Niedziela': 7
# }
# (Zamiana klucza z wartością i zostawienie tylko dni nieparzystych).
# Wynik przypisz na zmienną result


slownik = {
    1: 'Poniedziałek',
    2: 'Wtorek',
    3: 'Środa',
    4: 'Czwartek',
    5: 'Piątek',
    6: 'Sobota',
    7: 'Niedziela'
}
result = {}
for i in slownik:
    if int(i)%2 != 0:
        result[slownik[i]] = i


assert 'Poniedziałek' in result
