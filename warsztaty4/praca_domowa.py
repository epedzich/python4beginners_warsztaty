class DateError(Exception):
    def __init__(self):
        pass


class InvalidYearError(DateError):
    def __init__(self):
        pass


class InvalidMonthError(DateError):
    def __init__(self):
        pass


class InvalidDayError(DateError):
    def __init__(self):
        pass


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

        if isinstance(year, int):
            pass
        else:
            raise InvalidYearError

        if isinstance(month, int) and 0 < month < 12:
            pass
        else:
            raise InvalidMonthError

        if isinstance(day, int) and (
                        (0 < day < 29 and month == 2)
                    or (0 < day < 31 and month in (1, 3, 5, 7, 8, 10, 12))
                or (0 < day < 30 and month in (4, 6, 9, 11))
        ):
            pass
        else:
            raise InvalidDayError

#
# date = Date(30, 5, 2020)
# assert date.day == 30
# assert date.month == 5
# assert date.year == 2020
#
# try:
#     date2 = Date(40, 5, 2020)
# except InvalidDayError:
#     print('Błąd wyrzucony tak jak trzeba')
# else:
#     print('Bez błędu, a trzeba było :(')


def check_homework(capitals_csv, questions_csv, answers_csv):
    with open(capitals_csv, encoding='utf-8') as f:
        linie_stolic = f.read().splitlines()

    with open(questions_csv, encoding='utf-8') as f:
        linie_pytan = f.read().splitlines()

    with open(answers_csv, encoding='utf-8') as f:
        linie_odpowiedzi = f.read().splitlines()

    counter = 0

    for i, line in enumerate(linie_pytan):
        panstwo, odpA, odpB, odpC, odpD = line.split(';')

        for line in linie_stolic:
            country, capital = line.split(';')
            if country == panstwo:
                if capital == odpA:
                    popr_odp = 'A'
                elif capital == odpB:
                    popr_odp = 'B'
                elif capital == odpC:
                    popr_odp = 'C'
                else:
                    popr_odp = 'D'

        if popr_odp == linie_odpowiedzi[i]:
            counter += 1
        else:
            continue

    return counter
#
# assert check_homework('stolice.csv', 'pytania.csv', 'odpowiedzi.csv') == 5



# Chcemy napisać kod, który dla danego pliku z listą stolic wygeneruje number_of_sets zestawów pytań po number_of_questions_per_set pytań
# - Format listy stolic taki jak w stolice.csv
# - Format oczekiwanego pojedynczego zestawu pytań taki jak w pliku pytania.csv - prosimy pamiętać o nagłówkach
# - Każdy zestaw powinien znaleźć się w osobnym pliku - pierwszy w zestaw1.csv, drugi w zestaw2.csv itd (nie ma czegoś takiego jak zestaw 0)
# - pliki zestaw1.csv, zestaw2.csv itd. powinny się stworzyć w folderze z rozwiązaniem zadania (tzn. przy otwieraniu pliku nie podawać żadnej ścieżki, tylko samą nazwę pliku)
#
# Dodatkowe założenia:
# Pytanie o jeden kraj nie może wystąpić więcej niż raz (biorąc pod uwagę wszystkie zestawy)
# W przypadku, gdy ktoś poda nam dane, dla których musielibyśmy wygenerować więcej niż 48 pytań (tyle mamy stolic w pliku stolice.csv) - rzućmy ValueError
# Poprawna odpowiedź powinna znajdować się w losowej kolumnie - tzn. losowo powinna być odpowiedzią A, B, C lub D
# Do losowania należy skorzystać z modułu random https://docs.python.org/3/library/random.html
#
import csv
import random


def create_sets_of_question(capitals_csv, number_of_sets, number_of_questions_per_set):
    # Tu wpisz swoje rozwiązanie (i skasuj raise NotImplementedError() :)


    with open(capitals_csv, encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        panstwa = dict(reader)

    if number_of_questions_per_set * number_of_sets > len(panstwa):
        raise ValueError

    lista_panstw = list(panstwa)

    for i in range(number_of_sets):
        with open(f'zestaw{i+1}.csv', 'w', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';', lineterminator='\n')
            writer.writerow(['Państwo', 'A', 'B', 'C', 'D'])

            for i in range(number_of_questions_per_set):
                panstwo = random.choice(lista_panstw)
                lista_panstw.remove(panstwo)

                stolice = list(panstwa.values())
                stolica = panstwa[panstwo]
                random.shuffle(stolice)
                stolice.remove(stolica)
                zestaw = stolice[:3] + [stolica]
                random.shuffle(zestaw)

                writer.writerow([panstwo, *zestaw])
#
#
# with open('zestaw1.csv') as zestaw1:
#     reader = csv.reader(zestaw1, delimiter=';')
#     lines_count = 0
#     for row in reader:
#         print(row)
#         assert len(row) == 5  # 5 kolumn - Państwo + propozycje odpowiedzi A, B, C, D
#         lines_count += 1
#     assert lines_count == 9  # 8 pytan + naglowek
#
# try:
#     create_sets_of_question('stolice.csv', 5, 10)
# except ValueError:
#     print('Błąd wyrzucony tak jak trzeba')
# else:
#     print('Bez błędu, a trzeba było :(')


class Picture():
    def __init__(self, red, green, blue, width, height):

        self.width = width
        self.height = height

        self.pixels = [(r, g, b) for r, g, b in zip(red, green, blue)]


    def red(self):
        return tuple(r for r,g,b in self.pixels)

    def green(self):
        return tuple(g for r,g,b in self.pixels)

    def blue(self):
        return tuple(b for r,g,b in self.pixels)

    def size(self):
        return self.width, self.height

    def crop(self, x, y, width, height):
        new_picture = []

        for i in range(y, min(y + height, self.height)):
            for j in range(x, min(x + width, self.width)):
                new_picture.append(self.pixel(j, i))

        self.pixels = new_picture


    def pixel(self, x, y):
        i = self.width * y + x
        return self.pixels[i]

def test_one_red_pixel():
    red = [255]
    green = [0]
    blue = [0]
    width = 1
    height = 1
    obrazek = Picture(red=red, green=green, blue=blue, width=width, height=height)
    assert (1, 1) == obrazek.size()
    assert (255, ) == obrazek.red()
    assert (0, ) == obrazek.green()
    assert (0, ) == obrazek.blue()
    assert (255, 0, 0) == obrazek.pixel(0, 0)

def test_kwadrat_gradient():
    obrazek = Picture(red=range(256), green=range(256), blue=range(256), width=16, height=16)
    assert (16, 16) == obrazek.size()
    val = 0
    for y in range(16):
        for x in range(16):
            assert (val, val, val) == obrazek.pixel(x, y)
            val += 1

    # Same picture
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=16, height=16)
    obrazek_2.crop(0, 0, 16, 16) # powinniśmy dostać ten sam obrazek
    assert obrazek.red() == obrazek_2.red(), (obrazek.red(),  obrazek_2.red())
    assert obrazek.green() == obrazek_2.green()
    assert obrazek.blue() == obrazek_2.blue()

    # Left upper corner
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=16, height=16)
    obrazek_2.crop(0, 0, 1, 1)
    assert (0, ) == obrazek_2.red()
    assert (0, ) == obrazek_2.green()
    assert (0, ) == obrazek_2.blue()

    # right upper corner
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=16, height=16)
    obrazek_2.crop(15, 0, 1, 1)
    assert (15, ) == obrazek_2.red()
    assert (15, ) == obrazek_2.green()
    assert (15, ) == obrazek_2.blue()

    # right lower corner
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=16, height=16)
    obrazek_2.crop(15, 15, 1, 1)
    assert (255, ) == obrazek_2.red()
    assert (255, ) == obrazek_2.green()
    assert (255, ) == obrazek_2.blue()

    # left lower corner
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=16, height=16)
    obrazek_2.crop(0, 15, 1, 1)
    assert (240, ) == obrazek_2.red()
    assert (240, ) == obrazek_2.green()
    assert (240, ) == obrazek_2.blue()

    # 2x3 near lower corner
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=16, height=16)
    obrazek_2.crop(1, 12, 2, 3)
    assert (193, 194, 209, 210, 225, 226) == obrazek_2.red(), obrazek_2.red()
    assert (193, 194, 209, 210, 225, 226) == obrazek_2.green()
    assert (193, 194, 209, 210, 225, 226) == obrazek_2.blue()

    # 10x15 wystający → 3x5 lower right corner
    obrazek_2 = Picture(red=range(256), green=range(256), blue=range(256), width=16, height=16)
    obrazek_2.crop(13, 11, 10, 15)
    assert (189, 190, 191, 205, 206, 207, 221, 222, 223, 237, 238, 239, 253, 254, 255) == obrazek_2.red()
    assert (189, 190, 191, 205, 206, 207, 221, 222, 223, 237, 238, 239, 253, 254, 255) == obrazek_2.green()
    assert (189, 190, 191, 205, 206, 207, 221, 222, 223, 237, 238, 239, 253, 254, 255) == obrazek_2.blue()

if __name__ == '__main__':
    test_one_red_pixel()
test_kwadrat_gradient()