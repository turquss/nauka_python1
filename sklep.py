koszyk = [
    {'produkt':'guziki', 'ilosc':4, 'cena':8},
    {'produkt':'tasma', 'ilosc':6, 'cena':6.5},
    {'produkt':'suwak', 'ilosc':5, 'cena':2.5}
]

suma = 0
for poz in koszyk:
    il = poz['ilosc']
    c = poz['cena']
    suma = suma + (c * il)
    #print(c)
    #print(suma)
    #print(poz)

print(suma)
