from statistics import mean, median
from operator import attrgetter

# 1 uzduotis
sakinys = "The Zen of Python"

naujas = [x + "!" for x in sakinys.split()]
print(" ".join(naujas))

# 2 uzduotis
skaiciai = list(range(51))

padauginta = map(lambda x: x * 10, skaiciai)
print(list(padauginta))

dalinasi_is_septyniu = filter(lambda x: x % 7 == 0, skaiciai)
print(list(dalinasi_is_septyniu))

pakelta_kvadratu = map(lambda x: x ** 2, skaiciai)
skaiciai = list(pakelta_kvadratu)
print(skaiciai)

print(sum(skaiciai))
print(min(skaiciai))
print(max(skaiciai))
print(mean(skaiciai))
print(median(skaiciai))


print(sorted(skaiciai, reverse=True))

# 3 uzduotis
sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]

saraso_skaiciu_suma = sum(x for x in sarasas if type(x) is int or type(x) is float)
print(saraso_skaiciu_suma)

sudeti_zodziai = " ".join(zodis for zodis in sarasas if type(zodis) is str)
print(sudeti_zodziai)

loginiu_suma_sarase = sum(loginis for loginis in sarasas if type(loginis) is bool)
print(loginiu_suma_sarase)


# 4 uzduotis
class Zmogus:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def __repr__(self):
        return f'{self.vardas} {self.amzius}'


zmogus1 = Zmogus("Jonas", 33)
zmogus2 = Zmogus("Naglis", 26)
zmogus3 = Zmogus("Petras", 49)
zmogus4 = Zmogus("Lukas", 37)


zmoniu_sarasas = [zmogus1, zmogus2, zmogus3, zmogus4]

surusiuoti_vardai = sorted(zmoniu_sarasas, key=attrgetter('vardas'))
print(surusiuoti_vardai)

surusiuoti_metai = sorted(zmoniu_sarasas, key=attrgetter('amzius'))
print(surusiuoti_metai)


surusiuoti_vardai_atbulai = sorted(zmoniu_sarasas, key=attrgetter('vardas'), reverse=True)
print(surusiuoti_vardai_atbulai)

surusiuoti_metai_atbulai = sorted(zmoniu_sarasas, key=attrgetter('amzius'), reverse=True)
print(surusiuoti_metai_atbulai)

