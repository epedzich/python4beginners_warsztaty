# Stwórz listę 100 list, każda z liczbami od 1 do 100. Potem dla każdej j-tej
# z tych list wewnętrznych na jej końcu dodać sumę jej pierwszych elementów
# do j-tego włącznie.
# Spodziewany efekt: [ [1, 2, 3, ..., 100, 1], [1, 2, 3, ..., 100, 3],
# [1, 2, 3, ..., 100, 6], ..., [1, 2, 3, ..., 100, 5050] ]
# Wynikową listę przypisz na zmienną result

result = [(list(range(1, 101))) for i in range(1, 101)]

for j, x in enumerate(result):
    x.append(sum(x[:j + 1]))

assert result[-1][-1] == 5050
