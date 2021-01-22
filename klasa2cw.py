class Pozycja: # nazwa klasy to opis jak cos wyglada
    def __init__(self, nazwa, ilosc, cena):
        self.nazwa = nazwa
        self.ilosc = ilosc
        self.cena = cena

    def cena_calosc(self):
        return self.cena * self.ilosc

poz = Pozycja('mleko', 10, 10.0)
print(poz.cena_calosc())




class Produkty:
    def __init__(self, nazwa, ilosc, cena):
        self.nazwa = nazwa
        self.ilosc = ilosc
        self.cena = cena

    def cena_calosc(self):
        return self.cena * self.ilosc

poz = Produkty('cytryna', 12, 11.0)
print(poz.cena_calosc())
