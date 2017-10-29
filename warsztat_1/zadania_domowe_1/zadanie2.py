# Napisać kod tworzący listę list kolejnych elementów parzystych < 100 według
# schematu: [[0], [2], ... , [98]]. Wynikową listę przypisz na zmienną result.

result = [[i] for i in range(100) if i % 2 == 0]

assert result[1] == [2]
