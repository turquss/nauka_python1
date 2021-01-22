class Pozycja:
    def __init__(self, nazwa, ilosc, cena):
        self.nazwa = nazwa
        self.ilosc = ilosc
        self.cena = cena

    def cena_calosc(self):
        return self.cena * self.ilosc

poz = Pozycja('mleko', 10, 10.0)
print(poz.cena_calosc())
