# Stwórz listę liczb od 0 do 999.
# Liczby podzielne przez 3 zastąp słowem 'trzy'.
# Liczby podzielne przez 5 zastąp słowem 'pięć'.
# Liczby podzielne jednocześnie przez 3 i 5 zastąp słowem 'trzypięć'.
# Wynikową listę przypisz zmiennej result.

lista = list(range(1000))

result = lista

for i in lista:
    if i == 0:
        continue
    if i % 3 == 0:
        lista[i] = 'trzy'
    if i % 5 == 0:
        lista[i] = 'pięć'
    if i % 3 == 0 and i % 5 == 0:
        lista[i] = 'trzypięć'

assert result[15] == 'trzypięć'
