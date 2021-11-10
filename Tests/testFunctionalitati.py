from Logic.CRUD import adaugaRezervare
from Logic.functionalitati import ieftinireRezervari, pretMaximPentruFiecareClasa, ordonareDescrescatoareDupaPret, \
    sumePentruFiecareNume, trecereRezervareLaClasaSuperioara


def testTrecereRezervareLaClasaSuperioara():
    lista = []
    lista = adaugaRezervare("1", "Bugnariu Alice", "economy", "120", "nu", lista)
    lista = adaugaRezervare("2", "Andreea", "economy plus", "100", "da", lista)
    lista = adaugaRezervare("3", "Andreea", "economy", "100", "da", lista)
    assert trecereRezervareLaClasaSuperioara("Andreea",lista) == [[('id: ', '1'), ('nume: ', 'Bugnariu Alice'), ('clasa: ', 'economy'), ('pret: ', '120'), ('checkin: ', 'nu')], [('id: ', '2'), ('nume: ', 'Andreea'), ('clasa: ', 'business'), ('pret: ', '100'), ('checkin: ', 'da')], [('id: ', '3'), ('nume: ', 'Andreea'), ('clasa: ', 'economy plus'), ('pret: ', '100'), ('checkin: ', 'da')]]
testTrecereRezervareLaClasaSuperioara()
def testIeftiniri():
    lista = []
    lista = adaugaRezervare("1", "Bugnariu Alice", "economy", "120", "nu", lista)
    lista = adaugaRezervare("2", "Andreea", "business", "100", "da", lista)
    assert ieftinireRezervari(lista, 20) ==[[('id: ', '1'), ('nume: ', 'Bugnariu Alice'), ('clasa: ', 'economy'), ('pret: ', '120'), ('checkin: ', 'nu')], [('id: ', '2'), ('nume: ', 'Andreea'), ('clasa: ', 'business'), ('pret: ', 80.0), ('checkin: ', 'da')]]

testIeftiniri()
def testPretMaximPentruFiecareClasa():
    lista = []
    lista = adaugaRezervare("1", "Bugnariu Alice", "economy", "120", "nu", lista)
    lista = adaugaRezervare("2", "Andreea", "business", "100", "da", lista)
    assert pretMaximPentruFiecareClasa(lista) == (120, 0, 100)

testPretMaximPentruFiecareClasa()

def testOrdonareDescrescatoareDupaPret():
    lista = []
    lista = adaugaRezervare("1", "Bugnariu Alice", "economy", "120", "nu", lista)
    lista = adaugaRezervare("2", "Andreea", "business", "150", "da", lista)
    assert ordonareDescrescatoareDupaPret(lista) == [[('id: ', '2'), ('nume: ', 'Andreea'), ('clasa: ', 'business'), ('pret: ', '150'), ('checkin: ', 'da')], [('id: ', '1'), ('nume: ', 'Bugnariu Alice'), ('clasa: ', 'economy'), ('pret: ', '120'), ('checkin: ', 'nu')]]
testOrdonareDescrescatoareDupaPret()

def testSumePentruFiecareNume():
    lista = []
    lista = adaugaRezervare("1", "Bugnariu Alice", "economy", "120", "nu", lista)
    lista = adaugaRezervare("2", "Andreea", "business", "150", "da", lista)
    lista = adaugaRezervare("3", "Bugnariu Alice", "business", "150", "nu", lista)
    assert sumePentruFiecareNume(lista) == {'Bugnariu Alice': 270.0, 'Andreea': 150.0}

testSumePentruFiecareNume()